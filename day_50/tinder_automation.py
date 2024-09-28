from selenium import  webdriver
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
# WEB DRIVER
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/es")
login_btn = driver.find_element(By.XPATH, value='//*[@id="s-432461179"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()

facebook_btn = driver.find_element(By.CSS_SELECTOR, value='button[class="cxdzch5 f17p5q9z"]')
facebook_btn.click()

fb_login = driver.window_handles[1]
driver.switch_to.window(fb_login)

email_input =  driver.find_element(By.XPATH, value='//*[@id="email"]')
password_input =  driver.find_element(By.XPATH, value='//*[@id="pass"]')

email_input.send_keys("", Keys.ENTER)
password_input.send_keys("", Keys.ENTER)

