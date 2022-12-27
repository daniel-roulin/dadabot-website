import json
import sqlite3
from get_text import get_ex_text

with open("index.json") as f:
    index = json.load(f)

data = []
for chapter, exercises in index.items():
    for exercise in exercises.keys():
        print(f"Scanning exercise {exercise:3} on chapter {chapter:3}")
        content = get_ex_text(int(chapter), int(exercise))
        data.append((chapter, exercise, content))

print("Writing to database...")
con = sqlite3.connect("../frontend/database/database.db")
cur = con.cursor()
cur.executemany("INSERT INTO exercises (chapter_id, number, content) VALUES (?, ?, ?)", data)
con.commit() 
print("Done.")