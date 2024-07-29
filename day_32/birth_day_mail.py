import smtplib
import datetime as dt
import  pandas as pd
import random
my_email =""
my_password = ""
#date for today
today = (dt.datetime.now().month, dt.datetime.now().day)
# get birthdate
data = pd.read_csv("birthdays.csv")
birthdays = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}
person = birthdays[today]
if today in birthdays:
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        letter = file.read()
        letter = letter.replace("[NAME]",person["name"])
        print(letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject: Happy birthday\n\n{letter}")

# get template

#replace tamplate

#send mail