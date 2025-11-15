##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month

birthday_list = pd.read_csv("birthdays.csv")
birthday_dict = birthday_list.to_dict(orient="records")

for item in birthday_dict:
    if item["day"] == day and item["month"] == month:
        letter_num = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter_num}.txt", "r") as file:
            main_letter = file.read()
            upd_letter = main_letter.replace("[NAME]", f"{item["name"]}")

            my_email = "ajaytestacc12@gmail.com"
            password = "bmfgnlxbsctrpqoy"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=item["email"], msg=f"Subject: Happy Birthday {item["name"]}\n\n{upd_letter}")


