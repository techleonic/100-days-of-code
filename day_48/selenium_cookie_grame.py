from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('disable-dev-shm-usage')
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
def cookie_game():
    cookie = driver.find_element(By.ID, value="cookie")
    time_end = time.time()+5
    while time.time() < time_end:
        print(time.time())
        cookie.click()
    buy = driver.find_element(By.ID, value="buyCursor")
    buy.click()
    cookie_game()

cookie_game()