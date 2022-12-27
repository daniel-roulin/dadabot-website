# uvicorn api:app --reload
from fastapi import FastAPI
from fastapi.responses import FileResponse

from generator import create_pdf

app = FastAPI()


@app.get("/api")
def answer(chapter:int, exercise:int):
    create_pdf(chapter, exercise)
    return FileResponse("temp/answer.pdf")