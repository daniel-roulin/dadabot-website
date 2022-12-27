import json
import math
import re
import fitz


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

    final_rects = []
    if len(rects) != 1:
        print("Trying to fix bug")
        for rect in rects:
            print(rect)
            if math.floor(rect.x0) in (89, 109):
                final_rects.append(rect)
        print(final_rects[0])
    else:
        final_rects = rects

    if len(final_rects) > 1:
        print(f"Error: Too many matchs for exercise {exercise} on page {exercise_page_num} in chap {chapter}")
        raise
    elif len(final_rects) < 1:
        print(f"Error: No match for exercise {exercise} on page {exercise_page_num} in chap {chapter}")
        raise
    return final_rects[0]

def get_ex_text(chapter_int, exercise_int):
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
        page_range = 1 + (next_exercise_page_num - exercise_page_num)
    else:
        page_range = 1

    pdf = fitz.open(f"chapters/chap{chapter}.pdf")
    output = fitz.open()

    x, y, width, height = pdf.load_page(exercise_page_num).rect

    crop = fitz.Rect(0, 35, width, height - 115)
    page = output.new_page(-1, crop.width, crop.height * page_range)
    for i in range(page_range):
        page.show_pdf_page(crop + (0, crop.height * i, 0, crop.height * i), pdf, exercise_page_num + i, clip = crop)
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

    top = ex_rect.y0 - 8
    width = page.cropbox.width

    text = page.get_text(clip=fitz.Rect(0, top, width, bottom))

    output.close()

    return clean_text(text)

def clean_text(text):
    if len(text) == 0:
        return ""

    # Remove rare occurences of CHAPTERS appearing in the string
    pattern = r'\d+CHAPTER \d+\.'
    text = re.sub(pattern, '', text)

    # Remove char 65533 (invalid character)
    text = text.replace(chr(65533), "")

    # Remove new lines and tabs
    mapping = dict.fromkeys(range(32))
    text = text.translate(mapping)

    # Remove exercise number
    text = text.split(".", 1)[1]

    return text.strip()

if __name__ == "__main__":
    print(get_ex_text(1, 1))