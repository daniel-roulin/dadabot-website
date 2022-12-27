import json
import sqlite3

with open("chapter_names.json") as f:
    chapter_to_title = json.load(f)

data = []
for index, title in chapter_to_title.items():
    data.append((index, index, title, ""))

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.executemany("INSERT INTO chapters (id, number, title, image_path) VALUES (?, ?, ?, ?)", data)
con.commit() 