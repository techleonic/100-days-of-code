import smtplib

my_email = ""
Password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=Password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="",
                        msg="Subject:Hello\n\nHello this a message from python")