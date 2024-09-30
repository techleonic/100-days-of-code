import os
import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
Email = os.getenv("USER_NAME")
Password = os.getenv("PASSWORD")
print(Email, Password)
driver.get("https://www.instagram.com/")

#  <input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75"
#  class="_aa4b _add6 _ac4d _ap35" dir="" type="text" value="" name="username">


# <input aria-label="Password" aria-required="true" autocapitalize="off" autocorrect="off"
# class="_aa4b _add6 _ac4d _ap35" type="password" value="" name="password">
inputs  = driver.find_elements(By.CSS_SELECTOR, value='input._aa4b._add6._ac4d._ap35')

inputs[0].send_keys(Email)
inputs[1].send_keys(Password, Keys.ENTER)
time.sleep(3)
driver.get('https://www.instagram.com/python.utp/followers')

# class=" _acan _acao _acat _aj1- _ap30"
# class=" _acan _acao _acat _aj1- _ap30"
element = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
element.click()
# class=" _acan _acap _acas _aj1- _ap30"
# class=" _acan _acap _acas _aj1- _ap30"

buttons = driver.find_elements(By.CSS_SELECTOR, value='button._acan._acap._acas._aj1-._ap30')
top_ten_followers = buttons[0:9]
for followers in top_ten_followers:
    followers.click()