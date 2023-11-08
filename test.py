import requests
from bs4 import BeautifulSoup
import csv
import json

response = requests.get("https://ridibooks.com/category/new-releases/2200")

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.fig-rs5q24')
l = []
for no, book in enumerate(bookservices, 1):
    l.append(f"{no} {book.text.strip()}")


#파일을 한 번 쓴다.
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    json.dump(l, f_write, ensure_ascii=False, indent=4)

#파일을 다시 읽는다.
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
    line = f.readline()
    while line:
        data += line
        line = f.readline()
print(data)

#파일에 변수명을 추가하여 다시 쓴다.
final_data = f"var data = {data};"
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
    f_write.write(final_data)
