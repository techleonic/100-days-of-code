import csv
from bs4 import BeautifulSoup
import requests

url = "https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm"

page = requests.get(url=url)
page.raise_for_status()

# soup = BeautifulSoup(page.text, 'html.parser')
#
# table = soup.find("table")
#
# print(table)