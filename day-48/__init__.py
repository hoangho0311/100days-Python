import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B08CF8GMDQ/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
soup.select(selector=".a-price.a-text-price.a-size-medium.apexPriceToPay")
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

import smtplib

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 200

if price_as_float > 0:
    message = f"{title} is now {price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("hoanghv.21it@vku.udn.vn", "hoangcuqq")
        connection.sendmail(
            from_addr="hoanghv.21it@vku.udn.vn",
            to_addrs="hoanghv.21it@vku.udn.vn",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
        print("success")
