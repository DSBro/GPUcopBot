import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Amazon:
    email = ""
    password = ""
    def __init__(self):
        self.site = "https://www.amazon.com/EVGA-10G-P5-3897-KR-GeForce-Technology-Backplate/dp/B08HR3Y5GQ?ref_=ast_sto_dp"
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get(self.site)
        self.driver.find_element_by_xpath("/html/body/div[2]/header/div/div[1]/div[3]/div/a[2]/div/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ap_email"]').click()
        self.driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(self.email)
        self.driver.find_element_by_xpath('//*[@id="continue"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ap_password"]').click()
        self.driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
        input("Enter anything after loggin in")

    def checkStock(self):
        self.driver.get(self.site)
        arr = self.driver.find_elements_by_id('add-to-cart-button')
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
