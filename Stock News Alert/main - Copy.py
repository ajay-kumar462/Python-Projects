import requests
from twilio.rest import Client

account_sid = "#myaccountsid"
auth_token = "#myauthtoken"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY = "#apikey"
NEWS_API_KEY = "#newsapikey"


response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={API_KEY}")
response.raise_for_status()

# y_dt = input("Enter yesterday's date (eg. yyyy-mm-dd): ")
# dby_dt = input("Enter day before yesterday's date (eg. yyyy-mm-dd: ")

print(response.json())
y_close = float(response.json()["Time Series (Daily)"]["2025-10-13"]["4. close"])
dby_close = float(response.json()["Time Series (Daily)"]["2025-10-10"]["4. close"])

by_5 = y_close * 0.05
print(by_5)

if y_close > dby_close + by_5 or y_close < dby_close - by_5:
    threshold = 0
    news_response = requests.get(url="https://newsapi.org/v2/everything?q=tesla&from=2025-09-17&sortBy=publishedAt&"
                                     "apiKey=7cb7b1de104f4c498b98bf2067fb0cb3")
    news_response.raise_for_status()

    for item in news_response.json()["articles"]:
        if "Tesla" in item["title"] and threshold < 3:
            title = item["title"]
            desc = item["description"]
            print(f"Title: {title}")
            print(f"Desc: {desc}")

            client = Client(account_sid, auth_token)
            message = client.messages.create(
                messaging_service_sid='MG972d79b8ed1e95a3f1396433c20cfae6',
                body=f"\n{STOCK}: 🔺5% or 🔻5%\n"
                     f"Headline: {title}\n"
                     f"Brief: {desc}",
                from_="+14066268198",
                to='+919930340173'
            )

            print(message.status)
            threshold += 1


    # print(news_response.json()["articles"][0]["description"])
    # print(news_response.json()["articles"][1]["description"])
    # print(news_response.json()["articles"][2]["description"])

