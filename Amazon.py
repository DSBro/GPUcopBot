import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Amazon:
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=C:/Users/cbass/AppData/Local/Google/Chrome/User Data/")
        #options.add_argument("profile-directory=Profile 1")
        self.site = "https://www.amazon.com/EVGA-10G-P5-3897-KR-GeForce-Technology-Backplate/dp/B08HR3Y5GQ?ref_=ast_sto_dp"
        self.driver = webdriver.Chrome(options=options)

    def checkStock(self):
        self.driver.get(self.site)
        arr = self.driver.find_elements_by_id('add-to-cart-button')
        while not arr:
            arr = self.driver.find_elements_by_css_selector('button.style__addToCartBtn__nOP_z')
            self.driver.refresh()
            time.sleep(100000)
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
