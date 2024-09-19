from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('disable-dev-shm-usage')
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
# not close tab
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count  = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# article_count.click()

#FIND BY LINK TEXT
content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
content_portals.click()

#FILS INPUTS
search_input =  driver.find_element(By.NAME, value="search")
search_input.send_keys("Python",Keys.ENTER)

#SENDING NOT TEXT KEYS
# search_input.send_keys(Keys.ENTER)