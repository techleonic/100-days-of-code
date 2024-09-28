import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

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

# driver.get('https://www.speedtest.net/es')
#
# start_btn = driver.find_element(By.CSS_SELECTOR, value='a.js-start-test.test-mode-multi')
# start_btn.click()
# time.sleep(60)
# dowload_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
# upload_speed = driver.find_element(By.XPATH, value= '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
#
# print(dowload_speed, upload_speed)

driver.get('https://www.facebook.com/')
email =  driver.find_element(By.CSS_SELECTOR, value='input.inputtext._55r1._6luy')
email.send_keys(os.getenv("EMAIL"))
password = driver.find_element(By.CSS_SELECTOR, value='input.inputtext._55r1._6luy._9npi')
password.send_keys(os.getenv("PASSWORD"), Keys.ENTER)
post = driver.find_element(By.XPATH, value='//*[@id="scrollview"]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]')
post.click()
write = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]")
write.send_keys("My dowload speed is: 56 \nand my upload speed is: 12")

post_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div')
post_button.click()
driver.quit()
