import urllib.request
import json
import sqlite3
import webbrowser
import urllib.parse

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

with open("chapter_names.json") as f:
    chapter_to_title = json.load(f)

con = sqlite3.connect("../frontend/database/database.db")
cur = con.cursor()
for index, title in chapter_to_title.items():
    url = f"https://www.google.com/search?q={urllib.parse.quote(title)}+image&tbm=isch"
    webbrowser.open_new_tab(url)

    print()
    print(f"Chapter {index}: {title}")
    img_url = input("Image URL: ")

    # setting filename and image URL
    filename = f"../frontend/static/images/chapter{index}.jpg"

    # calling urlretrieve function to get resource
    urllib.request.urlretrieve(img_url, filename)
    
    cur.execute("UPDATE chapters SET image_path = ? WHERE number = ?;", (f"/images/chapter{index}.jpg", index))
    con.commit() 

con.close()