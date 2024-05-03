import requests
import os
from twilio.rest import Client

# stock symbole and name of the company
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# Stock API
StockAPIEndPoint = f"https://www.alphavantage.co/query"
STOCKINFO_APIKEY = "H50VNXFD21PJEPLG" # Get your API key from https://www.alphavantage.co/
# News API
NEWS_API = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "bdf3d970cd914df49ea0082f45419f61" # Get your API key from https://newsapi.org/
# Twilio Credentials
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH") # https://www.twilio.com/


para = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': STOCKINFO_APIKEY
}
respons = requests.get(StockAPIEndPoint, params=para)
respons.raise_for_status()
myjson = respons.json()
# print(myjson)

#-------------- Parsing the needed elements form the stock report ----------------#
daily = myjson['Time Series (Daily)']
firstTwo = list(daily.items())[:3]
yesterday = float(firstTwo[1][1]['4. close'])
before_yesterday = float(firstTwo[2][1]['4. close'])
print(yesterday)
print(before_yesterday)
print("--------------------------------------------------------------")


#-------------- Calculating the diference ----------------#
percentage_change = ((yesterday - before_yesterday) / before_yesterday) * 100


# checking if the stock's price increased or derecreased by 5%
if abs(percentage_change) >= 5:

    newsAPI_para = {
        'q': STOCK,
        'sortBy' : "publishedAt,relevancy",
        'apiKey' : NEWS_APIKEY,
        'language': 'en'
    }
    news_respons = requests.get(NEWS_API, newsAPI_para)
    news_respons.raise_for_status()
    news = news_respons.json()
    print(news)
    headline = news['articles'][0]['title']
    description = news['articles'][0]['description']

    # forma the message (SMS) depending on increase or decrease
    if percentage_change > 0:
        message = f"""
        {STOCK}: 🔺5%
        Headline: {headline}.
        Brief: {description}.
        """ 

    else:
        message = f"""
        {STOCK}: 🔻5%
        Headline: {headline}.
        Brief: {description}.
        """ 


    # Send message with twilio

    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body=message,
        from_='+14793163288',
        to='Your Number here'
    )
    print(message.status)

