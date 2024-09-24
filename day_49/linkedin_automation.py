import os
import time

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
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email_input = driver.find_element(By.ID, value="username")
password_input = driver.find_element(By.ID, value="password")

email_input.send_keys(os.getenv("EMAIL"),Keys.ENTER)
password_input.send_keys(os.getenv("PASSWORD"), Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4017397765&distance=25&f_AL=true&geoId=105517145&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
# job =  driver.find_element(By.XPATH, value='//*[@id="ember326"]')
# job.click()

# request_btn =  driver.find_element(By.ID, value='ember52')
# request_btn.click()

list_of_requestes = driver.find_elements(By.CSS_SELECTOR, value='a[class="disabled ember-view job-card-container__link job-card-list__title job-card-list__title--link"')
list_of_links = [request.get_attribute("href") for request in list_of_requestes if request.get_attribute("href")!= None]
print(list_of_links)
for link in list_of_links:
    driver.get(link)
    request_btn = driver.find_element(By.CSS_SELECTOR, value='button[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
    time.sleep(2)
    request_btn.click()

driver.quit()
# input_number = driver.find_elements(By.CSS_SELECTOR, value=".artdeco-text-input")
# print(input_number[0].text)