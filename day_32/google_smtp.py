import smtplib

my_email = ""
Password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=Password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="",
                        msg="Subject:Hello\n\nHello this a message from python")

import datetime as dt

now = dt.datetime.now()
year = now.year
month =  now.month
day_of_the_week = now.weekday()

day_of_birth = dt.datetime(year=1997,month=1,day=17)
print(day_of_birth)