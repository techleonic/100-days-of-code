import requests
from bs4 import BeautifulSoup
from datetime import datetime

user_input = input("enter date YYYY-MM-DD : ")
year, month, day = map(int,user_input.split("-"))
date = datetime(year=year,month=month, day=day).strftime("%Y-%m-%d")

url = f"https://www.billboard.com/charts/hot-100/{date}"

result = requests.get(url=url)

soup = BeautifulSoup(result.text, "html.parser")

list_of_titles = soup.select("div .o-chart-results-list-row-container")
list_of_songs = []
for tile in list_of_titles:
    song_number =  tile.find('span').getText().strip()
    song_name =  tile.find("h3").getText().strip()
    song_author =  tile.select_one("ul li ul li span").getText().strip()
    list_of_songs.append([song_number,song_name,song_author])

print(list_of_songs)