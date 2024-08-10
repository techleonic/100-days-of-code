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

print(twilio_isd)
print(twilio_token)
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#GETS YESTARDAY AND DAY BEFORE

yesterday =  datetime.now() - timedelta(1)
before_yesterday = datetime.now() - timedelta(2)
yesterday = str(datetime.strftime(yesterday, "%Y-%m-%d"))
before_yesterday = str(datetime.strftime(before_yesterday, "%Y-%m-%d"))
print(yesterday,before_yesterday)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": stock_apikey
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)

yesterday_stock = float( response.json()["Time Series (Daily)"][yesterday]["4. close"])


#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_stock = float( response.json()["Time Series (Daily)"][before_yesterday]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = yesterday_stock-before_yesterday_stock
percentage = (difference*100)/yesterday_stock

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



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

