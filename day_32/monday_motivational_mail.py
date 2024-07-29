import smtplib
import datetime as dt
import random

now = dt.datetime.now()

weekday = now.weekday()

my_email =""
my_password = ""


if weekday == 0:
    with open("quotes.txt","r", encoding="utf-8") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        quote=quote.encode(encoding="ascii",errors="replace")
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Monday Motivational Quotes\n\n{quote}")