import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('disable-dev-shm-usage')
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
# not close tab
chrome_options.add_experimental_option("detach", True)
# WEB DRIVER
driver = webdriver.Chrome(options=chrome_options)

result = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(result.text, "html.parser")
list_li = soup.find_all(name="li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
for li in list_li:
    price = li.find('span', {'data-test':'property-card-price'}).text.strip().replace("+","").replace("/mo","")
    address = li.find('address',{'data-test':'property-card-addr'}).text.strip()
    link = li.find('a',{'data-test':'property-card-link'}).get('href')
    print(price, address, link)

    driver.get('https://forms.gle/HZqGtKNoZfDx8wea7')
    inputs= driver.find_elements(By.CSS_SELECTOR, value='input.whsOnd.zHQkBf')
    price_input = inputs[0]
    link_input = inputs[1]
    address_input = driver.find_element(By.CSS_SELECTOR, value="textarea.KHxj8b.tL9Q4c")
    send_btn =  driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    time.sleep(3)
    price_input.send_keys(price)
    address_input.send_keys(address)
    link_input.send_keys(link)
    send_btn.click()

driver.quit()