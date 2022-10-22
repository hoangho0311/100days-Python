import requests
from twilio.rest import Client

account_sid = 'AC2224dcf8cdfd3eac664be83cf214f2aa'
auth_token = '7be5f0a5067a81eb3ce34961ed2ccd3b'

api_key ="UGQUARVCNA09G4UX"
news_api_key = "cfb8176d2d294cbd809ab751e9b7a954"
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":api_key
}
respone = requests.get("https://www.alphavantage.co/query", params=stock_params)
data = respone.json()["Time Series (Daily)"]
data_list = [value for (ket,value) in data.items()]

yesterday_data = data_list[0]
yesterday_data_closing = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing = day_before_yesterday["4. close"]

difference = abs(float(yesterday_data_closing)- float(day_before_yesterday_closing))
diff_percent = (difference/float(yesterday_data_closing))*100

if diff_percent<1:


    news_params ={
        "apikey":news_api_key,
        "qInTitle":"Tesla Inc"
    }
    new_resonse = requests.get("https://newsapi.org/v2/everything", params=news_params)
    article = new_resonse.json()["articles"]
    three_article = article[:3]

    format_article = [f"Headline: {article['title']}.\nBrief:{article['description']}" for article in three_article]
    client = Client(account_sid, auth_token)
    for article in format_article:
        message = client.messages \
            .create(
            body=article,
            from_='+18315746342',
            to='+84822988755'
        )
    print("succes")
