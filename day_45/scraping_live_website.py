from bs4 import BeautifulSoup
import requests
from pathlib import Path
import csv

url = "https://news.ycombinator.com/"

response =  requests.get(url=url)
soup = BeautifulSoup(response.text,"html.parser")

titles = soup.find_all(class_="titleline")
data= []
headers = ["Title","link"]
list_of_data = []
for title in titles:
    list_of_data.append([title.getText(), title.a.get("href")])



path = Path("hacker_news.csv")
if not path.exists():
    with open(path,mode="w", newline="") as file:
        data.append(headers)
        data += list_of_data
        writer = csv.writer(file)
        writer.writerows(data)
else:
    for title in titles:
        with open(path,"a", newline="") as file:
            writer = csv.writer(file)
            for data in list_of_data:
                writer.writerow([data[0],data[1]])