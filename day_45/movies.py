import requests
from bs4 import BeautifulSoup
results = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(results.text, "html.parser")

list_of_text = [ f"{movies.getText()}\n" for movies in soup.find_all(name="h3") ]
list_of_text.reverse()
with open("movies.txt", mode="w") as file:
    file.writelines(list_of_text)
