
#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



###---IMPORTS---###

import pandas
import datetime as dt
import random
import smtplib

###---DATA SOURCES---###
bday_data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in bday_data.iterrows()}


today = dt.datetime.now()
today_date = (today.month, today.day)
print(today_date)

my_email = "robertobobsono@gmail.com"
email_pw = "nice_try_no"


###---CHECK BDAY LOGIC---###
if today_date in bday_dict:
    bday_name = bday_dict[today_date]
    print(bday_name['name'])
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as bday_card:
        contents = bday_card.read()
        print(contents)
        bday_card_final = contents.replace("[NAME]", bday_name["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bday_name["email"],
            msg=f"Subject: Happy Birthday!\n\n{bday_card_final}"
        )



# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




