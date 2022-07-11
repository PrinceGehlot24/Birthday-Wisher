# import smtplib
#
# my_email = "****8@yahoo.com"
# my_pass = "iaqkmcxqkzusfc"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#     connection.starttls()
#     # connection.connect("smtp.gmail.com",27,my_email)
#     connection.login(user=my_email, password=my_pass)
#     connection.sendmail(from_addr=my_email, to_addrs="*****@gmail.com", msg="subject:Dummy\n\n hi hello.")


import datetime as dt
import random
import smtplib


MY_EMAIL = "*****@gmail.com"
MY_PASSWORD = "12**456@asdf"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", encoding="utf8") as quote_files:
        all_quotes = quote_files.readlines()
        quotes = random.choice(all_quotes)
        quote = quotes.encode('ascii', 'ignore').decode('ascii')
        print(quote)

        with smtplib.SMTP("smtp.gmail.com", 587) as con:
            con.starttls()
            con.login(MY_EMAIL, MY_PASSWORD)
            con.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"subject:Monday Motivation\n\n{quote}")
