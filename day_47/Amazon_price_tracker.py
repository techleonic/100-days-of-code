import os
from flask import flask
import  requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

#TODO: SHEETY SAVE PRODUCT DATA




# TODO:GET ARTICLE PAGE FROM AMAZON
url = "https://www.amazon.com/dp/B0CNFL6YGH/?coliid=I2XQOHS70R8VB9&colid=384NAPVWS0LR1&psc=1&ref_=list_c_wl_lv_o"
article_code= url.split("dp/")[1].split("/")[0]
results =  requests.get(url=url)
product_page = results.text


#TODO: PRODUCT SOUP
product_soup = BeautifulSoup(product_page, "html.parser")
product_title = product_soup.find(name="span",id="productTitle").get_text().strip()
product_price = product_soup.find(name="span", class_="a-price-whole").get_text().strip() +product_soup.find(name="span",class_="a-price-fraction").get_text().strip()
f_product_price = float(product_price.replace(",", ""))
print(product_title, f_product_price, url)

#TODO: SHEETY INSERT DATA INTO THE GOOGLE SHEET
head ={
    "Authorization": os.getenv("TOKEN")
}
print(head)
body = {
    "hoja1":{
        "productCode":article_code,
        "productName": product_title,
        "productUrl" : url,
        "entryPrice" : f_product_price,
        "lowestPrice": 0,
        "highestPrice":0,
        "currentPrice" : 0
    }
}
SHEETY_ENDPOINT = "https://api.sheety.co/cd1a064e0f44ab9c6aca48b4624dcb9a/priceTracker/hoja1"\

sheety_result  = requests.post(url=SHEETY_ENDPOINT,headers=head,json=body)
print(sheety_result)







# camel_endpoint = "https://camelcamelcamel.com/product/"+article_code
# with sync_playwright() as p:
#     #launch the browser
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#
#     #navigate to the page
#     page.goto(camel_endpoint)
#
#     #wait for the page to load
#     page.wait_for_load_state("load")
#
#     #get content from the page
#     content = page.content()
#
#     #parese the content with BeutifullSoup
#     camel_soup = BeautifulSoup(content, "html.parser")
#     print(camel_soup.prettify())

