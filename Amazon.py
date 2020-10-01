import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Amazon:
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=C:/Users/cbass/AppData/Local/Google/Chrome/User Data/")
        #options.add_argument("profile-directory=Profile 1")
        self.site = "https://www.amazon.com/stores/page/CFF83A4D-9DEC-4003-AC7E-96DF4170CED0?ingress=0&visitId=158b1f34-0594-496b-b609-a1a5d0754bb0"
        self.driver = webdriver.Chrome(options=options)

    def checkStock(self):
        self.driver.get(self.site)
        arr = self.driver.find_elements_by_css_selector('button.style__addToCartBtn__nOP_z')
        while not arr:
            arr = self.driver.find_elements_by_css_selector('button.style__addToCartBtn__nOP_z')
            self.driver.refresh()
            time.sleep(60)
        arr[0].click()

    def buyItem(self):
        self.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
        #self.driver.find_element_by_name('proceedToRetailCheckout').click()
        #address
        #self.driver.find_element_by_id("orderSummaryPrimaryActionBtn-announce").click()
        #credit card
        #self.driver.find_element_by_id("orderSummaryPrimaryActionBtn-announce").click()
        #buy
        self.driver.find_element_by_id("submitOrderButtonId-announce").click()
        print("Purchased!")
