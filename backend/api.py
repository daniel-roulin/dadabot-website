# uvicorn api:app --reload
from fastapi import FastAPI
from fastapi.responses import FileResponse
from enum import Enum
from generator import create_response


class Format(str, Enum):
    pdf = "pdf"
    img_light = "img-light"
    img_dark = "img-dark"


class Format(str, Enum):
    pdf = "pdf"
    img_light = "img-light"
    img_dark = "img-dark"


app = FastAPI()


@app.get("/api")
def answer(chapter: int, exercise: int, output_format: Format = Format.img_light):
    path = create_response(chapter, exercise, output_format.value)
    return FileResponse(path)