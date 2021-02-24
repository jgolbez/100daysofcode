import smtplib
import datetime as dt
import random


#####---- DETERMINE DATE/TIME ----####
now = dt.datetime.now()
day_of_week = now.weekday()

#####---- READ QUOTES ----####
def generate_quote():
    with open("quotes.txt", 'r') as quotes:
        quote_list = quotes.readlines()
        daily_quote = random.choice(quote_list)
        return daily_quote


#####---- COMPOSE MAIL ----####

def send_mail():
    motiv_quote = generate_quote()
    my_email = "robertobobsono@gmail.com"
    email_pw = "nice_try_no"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jgolbez@gmail.com",
            msg=f"Subject: Daily Motivational Quote\n{motiv_quote}"
        )

#####---- MAIN - CHECK DATE AND SEND MAIL ON CORRECT DAY ----####

if day_of_week == 0:
    send_mail()




