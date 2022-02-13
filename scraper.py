from bs4 import BeautifulSoup
import requests
import lxml

PRODUCT_URL = "https://www.amazon.in/Gigabyte-GeForce-2060-GDDR6-Graphics/dp/B08CRZTTBZ/ref=sr_1_1?crid=NUT888REIBLB&keywords=rtx+2060&qid=1643278179&sprefix=rtx+2060%2Caps%2C275&sr=8-1"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Encoding": "gzip, deflate"
}


class Scraper:
    """Class to scrape price of an item from Amazon"""

    def __init__(self):
        self.url = PRODUCT_URL
        self.headers = HEADERS

    def get_price(self):
        """gets and price and title of the product and returns a tuple"""
        response = requests.get(url=self.url, headers=self.headers)
        webpage = response.text

        soup = BeautifulSoup(webpage, "lxml")

        product_title = soup.find(name="span", id="productTitle").get_text().strip()
        product_price = soup.find(name="span", class_="a-price-whole").get_text().split('.')[0]
        product_price = int(product_price.replace(',', ''))
        return (product_price, product_title)

