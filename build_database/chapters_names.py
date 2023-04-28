import json
from bs4 import BeautifulSoup

# https://bcs.wiley.com/he-bcs/Books?action=contents&itemId=0471320005&bcsId=1074
with open("chapter.html") as f:
    soup = BeautifulSoup(f, "html.parser")

# divs = soup.find_all('div', class_="chapterTitle")
# print(divs)

chapter_to_title = {}
h3s = soup.select("div.chapterTitle h3")
for h3 in h3s:
    text = h3.text
    words = text.split(" ")
    number = words[1][:-1]
    parts = text.split(":")
    title = parts[1].strip()
    chapter_to_title[int(number)] = title

print(chapter_to_title)

with open("chapter_names.json", "w") as f:
    json.dump(chapter_to_title, f, indent=4)