from selenium import webdriver
from selenium.webdriver.common.by import  By
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

driver.get("https://www.python.org/")

events =  driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
print(events.text)
list_of_evetns = events.text.split("\n")
events_dict = {}
number=0
for i in range(1,10,2):
    events_dict[number]= {"time":list_of_evetns[i-1],"name":list_of_evetns[i]}
    number+=1

print(events_dict)
driver.quit()
