from datetime import datetime
import pandas
import random
import smtplib

my_email = "******@yahoo.com"
my_pass = "wmkizf57ykbejnyp"

receiver = "******@gmail.com"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dictionary = {(data_rows["month"], (data_rows["day"])): data_rows for (index, data_rows) in data.iterrows()}

if today_tuple in birthday_dictionary:
    birthday_person = birthday_dictionary[today_tuple]
    file_path = f"Birthday_templates/Letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("NAME", birthday_person["name"])

    with smtplib.SMTP("smtp.yahoo.mail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver,
                            msg=f"Subject:Happy Birthday!\n\nhello")


