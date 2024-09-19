from selenium import webdriver
from selenium.webdriver.common.by import By

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

#TODO: SCRAPING AMAZON PRICE By.CLASS_NAME
# driver.get("https://www.amazon.com/dp/B0CL5G57D8/?coliid=I95E7FQO640V8&colid=3KSHLDSG1YCZO&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it")
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(price,cents)
# # closes a single tab
# # driver.close()
# #closes al tabs`
# driver.quit()

#TODO: SCRAPING PYTHON By.NAME
driver.get("https://www.python.org/")

#TODO:FIND BY NAME
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.text)

#TODO: GET ATTRIBUTE
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")

#TODO: GET SIZE
print(button.size)

#TODO: GET ELEMENT BY CSS SELECTOR
docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(docs_link.text)

#TODO: GET ELEMENT BY XPATH
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.get_property("href"))

driver.quit()


