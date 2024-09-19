import os

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
import easyocr

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

    all_headers = {
        ":authority": "www.amazon.com",
        ":method": "GET",
        ":path": "/hz/wishlist/ls/HQUMSYI1CRRP/ref=nav_wishlist_lists_2",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "cookie": 'aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1714582344860-147872.44_0; regStatus=pre-register; session-id=131-2742780-9383028; ubid-main=133-4932664-3314317; lc-main=en_US; x-main="E@ckE6iL?jY1v9QOZL74Q98VWl4VaEJu77iCUisXXr2xjwLNe95iVmoH0mO70EL5"; at-main=Atza|IwEBIOWegiad7obnbxwzXZIfS6SmOH87DhzpgMhjmnU3H4uZ8gz4nmVf0cy7KddovRI62eMDhrZaLy2h91leMPJpq_nKK1G_DEvNUpEmZN0WRO8mSi170BTsvOsF_CQv7cjXe_B7goCFgzUEl1zl3zNmy1UXfy7IYPY2Us72CTFisxTIWCtHuvEdqBh5Jc25vVxUQ27aO_ZRQmepPh48R7zBrr8q4kkluPscyXkHgImXuyq_SA; sess-at-main="c4qXY6bNQRA7069MWnHRcHXsAftmVnW294fCP5Rn2CA="; sst-main=Sst1|PQFe4L9bQxMsTjnei08a3SIQCev0NtTPkxYFCZ1pk8dl2piCgagJns78sUzx_SRBhUNCN4PI9VaDhp3YqMK274Xtzi53ls9B_C1MPTjv1g2ftJ_F7GlfLWEYTifhxMqxy5Sf0JvFoS1P4i_pp-pWtaE4GNbkFbIoFU2LYQjG-PS6YiC8MC7eds253dK-589TMd0GlQcVGKYOk171TFcDtMraj2zn0zOal2naeEIN1Vwr2iA-PBerQ2TR-ai9BjeiKwj5pv2r7mFfOUH-k0HBWf1XTYOYDTbpBhvOOqRwfUA9fVo; session-id-time=2082787201l; i18n-prefs=USD; aws-ubid-main=850-6861481-7068717; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19981%7CMCMID%7C61442261875455912621297160986857391612%7CMCAAMLH-1726946492%7C4%7CMCAAMB-1726946492%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1726348892s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; session-token=QHuJZ3NnlEghUEmdmhy6WlagKK44RSxf8mDxttqGgDKlb2X/mNKRZ52lEchibd0OyTSCOvE0NeXqPOgNI2LHg1kkEx8bzCoHX38Qjzivo6VRGVSu4rvlIb8Z71FUbdxDZyPrv7pScB84M+3NbZIZ2ny8lpTsbNnrIgvwzhKkDm9PWoy/lODk+Lm0afAcqPWcEn9mt6oljmR2QBhBULFh9vUi6pV46WzAQ8UJPt0M6EBe6AW/FGplzbemJ59C4n2v4SBGuUBMLp2SM5odwtOjRTaPb8bKywI3nuSFlQEk+jrq0LTx1PPDqy4KcqS/e9bVHkbqjb3ksI9nDLh5dRs/cyFTA/4xMLPhItF9rORu2xdUDYUJ904rEooA+rDsnOh9; csm-hit=tb:MC1GS2TEJAMVA96K92DM+s-MC1GS2TEJAMVA96K92DM|1726424234875&t:1726424234875&adb:adblk_no',
        "device-memory": "8",
        "downlink": "5.05",
        "dpr": "1",
        "ect": "4g",
        "priority": "u=0, i",
        "rtt": "100",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-platform-version": '"6.0"',
        "sec-ch-viewport-width": "858",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
        "viewport-width": "858"
    }

    results = requests.get(url=url, headers=custom_headers)
    # print(results.raise_for_status())
    product_page = results.text
    with open("response.html", "w", encoding="utf-8") as file:
        file.write(product_page)

    print("it got the page")

    #TODO: PRODUCT SOUP
    product_soup = BeautifulSoup(product_page, "html.parser")

    #TODO: RESOLVE DE CATCHA
    if(product_soup.find(name="form", attrs={"action":"/errors/validateCaptcha"}) != None):
        catcha_img = product_soup.find(name="img").get("src")
        amzn_tag, amzn_r_tag = product_soup.find_all(name="input", attrs={"type": "hidden"})
        amzn = amzn_tag.get("value")
        amzn_r = amzn_r_tag.get("value")


        captcha_url = catcha_img
        response = requests.get(captcha_url)
        img = Image.open(BytesIO(response.content))

        # TODO:IMAGE TO TEXT
        reader = easyocr.Reader(['en'], gpu=False)
        text_detections = reader.readtext(img, detail=0)
        print()
        # return ("<h1>"+f"amzn: {amzn} amznr: {amzn_r}   Catcha link: {catcha_img}   link: {amazon_link} text_detection:{text_detections[0]}</h1>")


        #TODO: SUBMIT THE CATCHA
        submit_url = "https://www.amazon.com/errors/validateCaptcha"
        form_data = {
            "amzn": amzn,
            "amzn-r": amzn_r,
            "field-keywords": text_detections[0].strip()  # Submit the CAPTCHA text from OCR
        }

        catcha_response = requests.get(submit_url, params=form_data)
        product_soup =BeautifulSoup( catcha_response.text, "html.parser")
        with open("aftercatcha.html", "w", encoding="utf-8") as file:
            file.write(catcha_response.text)

        print("catcha Resolve")

    product_title = product_soup.find(name="span",
                                      id="productTitle").get_text().strip()
    product_price = product_soup.find(
        name="span",
        class_="a-price-whole").get_text().strip() + product_soup.find(
            name="span", class_="a-price-fraction").get_text().strip()
    f_product_price = float(product_price.replace(",", ""))

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
