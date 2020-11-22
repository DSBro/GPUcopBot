import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import config
client = Client(config.account_sid, config.auth_token)
class Zotac:

    def any_in_stock(self):
        request = requests.get('https://www.zotacstore.com/us/graphics-cards/geforce-rtx-30-series')
        soup = BeautifulSoup(request.content,'html.parser')
        products = soup.find("div", {"class" : "category-products"})
        check_all = products.find_all("div",{"class" : "wrapper-hover"})
        if len(products.find_all("button")) > 0:
            client.messages.create(
                body="somethings in stock",
                from_=config.twilioNumber,
                to=config.myNumber
            )
            return True
        # for gpu in check_all:
        #     if gpu.find_all("button"):
        #         s = gpu.find_all("a")[1].getText() + " is in stock"
        #         client.messages.create(
        #             body=s,
        #             from_=config.twilioNumber,
        #             to=config.myNumber
        #         )
