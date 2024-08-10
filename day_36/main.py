import requests
import  os
from datetime import  datetime,timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
twilio_isd = os.environ.get("TWILIO_SID")
twilio_token =  os.environ.get("TWILIO_TOKEN")
news_apikey = os.environ.get("NEWS_APIKEY")
stock_apikey = os.environ.get("STOCK_APIKEY")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#GETS YESTARDAY AND DAY BEFORE

yesterday =  datetime.now() - timedelta(1)
before_yesterday = datetime.now() - timedelta(2)
yesterday = str(datetime.strftime(yesterday, "%Y-%m-%d"))
before_yesterday = str(datetime.strftime(before_yesterday, "%Y-%m-%d"))

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": stock_apikey
}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
yesterday_stock = float( response.json()["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_stock = float( response.json()["Time Series (Daily)"][before_yesterday]["4. close"])


difference = yesterday_stock-before_yesterday_stock

percentage = (difference*100)/yesterday_stock

stock_info = f"{STOCK_NAME} {"⬆️"if percentage > 0 else "⬇️"} {round(percentage, 2)}%"

news_params = {
    "q": STOCK_NAME,
    "apiKey": news_apikey,
    "language":"en",
    "pageSize":3
}

response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
articles = response.json()["articles"]
for article in articles :
    try:
        from twilio.rest import Client
        account_sid =   twilio_isd
        auth_token = twilio_token
        client = Client(account_sid, auth_token)
        msg = f"{stock_info}\n{article["title"]}\n{article["description"]}"
        message = client.messages.create(
            from_='+19787231024',
            body=msg,
            to='+50586287283'
        )
        print(message.error_message)
    except:
        print("something went wrong")


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

