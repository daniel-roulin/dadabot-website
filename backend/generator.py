import json
import os
import PIL
import fitz
import pdfCropMargins
import pdf2image


class InvalidChapter(Exception):
    pass


class InvalidExercise(Exception):
    pass


class InternalError(Exception):
    pass


def find_ex_rect(page, exercise, exercise_page_num, chapter):
    """Returns the rectangle around a given exercise"""
    matches = page.search_for(f"{exercise}. ")
    rects = []
    for n in range(len(matches)):
        if matches[n].x0 < 110:
            rects.append(matches[n])
    if len(rects) > 1:
        print(f"Error: Too many matches for exercise {exercise} on page {exercise_page_num} in chap {chapter}")
        raise
    elif len(rects) < 1:
        print(f"Error: No match for exercise {exercise} on page {exercise_page_num} in chap {chapter}")
        raise
    return rects[0]


def create_response(chapter_int, exercise_int, output_format):
    """Takes a chapter and exercise number and creates a PDF of the exercise"""

    chapter = str(chapter_int)
    exercise = str(exercise_int)
    next_exercise = str(exercise_int + 1)

    with open("index.json") as f:
        index = json.load(f)

    if not chapter in index:
        raise InvalidChapter
    elif not exercise in index[chapter]:
        raise InvalidExercise

    exercise_page_num = index[chapter][exercise]

    if next_exercise in index[chapter]:
        next_exercise_page_num = index[chapter][next_exercise]
        page_range = 1 + (next_exercise_page_num-exercise_page_num)
    else:
        page_range = 1

    pdf = fitz.open(f"chapters/chap{chapter}.pdf")
    output = fitz.open()

    x, y, width, height = pdf.load_page(exercise_page_num).rect

    crop = fitz.Rect(0, 35, width, height - 115)
    page = output.new_page(-1, crop.width, crop.height*page_range)
    for i in range(page_range):
        page.show_pdf_page(crop + (0, crop.height*i, 0, crop.height*i), pdf, exercise_page_num + i, clip=crop)
    pdf.close()

    page = output.load_page(0)

    try:
        ex_rect = find_ex_rect(page, exercise, exercise_page_num, chapter)
        if next_exercise in index[chapter]:
            next_ex_rect = find_ex_rect(page, next_exercise, exercise_page_num, chapter)
            bottom = next_ex_rect.y0 - 8
        else:
            bottom = height
    except Exception as e:
        raise InternalError

    highlight_rect = page.search_for(f"{exercise}.", clip=ex_rect)[0]
    highlight = page.add_highlight_annot(highlight_rect)
    if output_format == "img-dark":
        highlight.set_colors(stroke=(0.0, 0.5, 1.0))
    else:
        highlight.set_colors(stroke=(1.0, 0.5, 0.0))
    highlight.update()

    top = ex_rect.y0 - 8
    width = page.cropbox.width
    page.set_cropbox(fitz.Rect(0, top, width, bottom))

    os.makedirs("temp", exist_ok=True)
    output.save("temp/temp.pdf", deflate=True, garbage=3)
    pdfCropMargins.crop(["temp/temp.pdf", "-o", "temp/answer.pdf"])

    if output_format == "pdf":
        return "temp/answer.pdf"
    elif "img" in output_format:
        image = pdf2image.convert_from_path("temp/answer.pdf")[0]
        if output_format == "img-dark":
            image = PIL.ImageOps.invert(image)
        image.save("temp/answer.png")
        return "temp/answer.png"