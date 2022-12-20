import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704. 103 Safari/537.36"
}

response = requests.get(
    'https://www.amazon.com.br/PlayStation®5-God-of-War-Ragnarök/dp/B0BLW5C5KN/ref=sr_1_3?keywords=playstation+5&qid=1671499647&sprefix=plays%2Caps%2C156&sr=8-3&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147', headers=headers
)
soup = BeautifulSoup(response.content, 'html.parser')

def check_price():
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text().strip()
    print('Product name & specs: ', title.strip())
    print('Product cost:', price)
check_price()