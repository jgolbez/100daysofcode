###--- Imports ---###
# Decouple - Pull environment variables/data
from decouple import config

# Requests - API Requests
import requests

# Twilio - For SMS
from twilio.rest import Client


###--- Data Sources/Global Variables ---###
ALPHA_API_KEY = config('ALPHA_API_KEY')
NEWSAPI_API_KEY = config('NEWSAPI_API_KEY')
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY,
}
news_parameters = {
    "q": f"{COMPANY_NAME}",
    "sortBy": "publishedAt",
    "apiKey": NEWSAPI_API_KEY,
}
#Twilio API
account_sid = config('TWILIO_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
twilio_phone = config('TWILIO_PHONE_NUMBER')
test_phone = config('TEST_PHONE_NUMBER')


###--- Functions ---###

# Stock Pull
def stock_pull():
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    stock_dict = response.json()['Time Series (Daily)']
    close_price = [float(v['4. close']) for (k,v) in stock_dict.items()]
    return close_price

# Calculate Stock Data for Notifications
def calc_stock(close_price):
    diff_price = round(abs(close_price[0] - close_price[1]), 2)
    print(f"Dollar Difference: {diff_price}")
    pct_diff = round(abs(close_price[0] - close_price[1])/close_price[1]*100, 2)
    print(f"Pct Difference: {pct_diff}")
    if close_price[0] > close_price[1]:
        stock_arrow = "🔺"
    elif close_price[0] < close_price[1]:
        stock_arrow = "🔻"
    else:
        stock_arrow = "="
    return diff_price, pct_diff, stock_arrow

# News Pull
def pull_news_headline():
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_list = response.json()['articles']
    format_news_dict = news_list[:3]
    article_headline = [headline['title'] for headline in format_news_dict]
    return article_headline

def pull_news_description():
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_list = response.json()['articles']
    format_news_dict = news_list[:3]
    article_description = [description['description'] for description in format_news_dict]
    return article_description

def text_news(stock, news_h, news_d) -> list:
    for msg in range(0,3):
        news_text = f"{STOCK_NAME} {stock[1]}% {stock[2]}\n" \
           f"Headline: {news_h[msg]}\nBrief: {news_d[msg]}"
        message = client.messages \
            .create(
            body=news_text,
            from_=f"+{twilio_phone}",
            to=f"+{test_phone}"
        )
        print(message.status)








#Main Loop

stock_close_price = stock_pull()
stock_tuple = calc_stock(stock_close_price)
print(stock_tuple)
news_headline = pull_news_headline()
news_description = pull_news_description()
text_news(stock_tuple, news_headline, news_description)

#msg_body = text_news(stock_tuple, news_tuple)
#print(msg_body)
#if stock_tuple[1] > 5:
#    news_tuple = pull_news()
#    text_body = format_news(stock_tuple, news_tuple)






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

