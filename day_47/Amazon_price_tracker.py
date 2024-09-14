import os

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

#TODO:CONFIGURE FLASK APP
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def home_post():
    amazon_link = request.form["amazon_link"]
    # TODO:GET ARTICLE PAGE FROM AMAZON
    url = amazon_link
    article_code = url.split("dp/")[1].split("/")[0]
    custom_headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Accept-Language': 'da, en-gb, en',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'https://www.google.com/'
    }
    results = requests.get(url=url, headers=custom_headers)
    product_page = results.text

    #TODO: PRODUCT SOUP
    product_soup = BeautifulSoup(product_page, "html.parser")
    product_title = product_soup.find(name="span",
                                      id="productTitle").get_text().strip()
    product_price = product_soup.find(
        name="span",
        class_="a-price-whole").get_text().strip() + product_soup.find(
            name="span", class_="a-price-fraction").get_text().strip()
    f_product_price = float(product_price.replace(",", ""))
    print()

    #TODO: SHEETY INSERT DATA INTO THE GOOGLE SHEET
    head = {"Authorization": os.environ['TOKEN']}
    print(head)
    body = {
        "hoja1": {
            "productCode": article_code,
            "productName": product_title,
            "productUrl": url,
            "entryPrice": f_product_price,
            "lowestPrice": f_product_price,
            "highestPrice": f_product_price,
            "currentPrice": f_product_price
        }
    }
    SHEETY_ENDPOINT = "https://api.sheety.co/cd1a064e0f44ab9c6aca48b4624dcb9a/priceTracker/hoja1"\

    sheety_result = requests.post(url=SHEETY_ENDPOINT, headers=head, json=body)
    json_response = sheety_result.json()

    return render_template(
        "index.html",
        output=
        f"""SAVED! Code: {article_code} Product: {product_title}Price: {f_product_price}""",
        api_response=json_response)


if __name__ == "__main__":
    app.run()
