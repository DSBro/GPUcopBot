import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Newegg:
    email = ''
    password = ''
    cvv = ''

    def __init__(self):
        self.site = 'https://www.newegg.com/p/pl?d=rtx+3070&N=100007709&isdeptsrh=1'
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get(self.site)

        self.driver.find_element_by_xpath("/html/body/div[7]/header/div[1]/div[4]/div[1]/div[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="labeled-input-signEmail"]').click()
        self.driver.find_element_by_xpath('//*[@id="labeled-input-signEmail"]').send_keys(self.email)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/form/div/div[3]/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="labeled-input-password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/form/div/div[3]/button').click()
        time.sleep(2)



    def checkStock(self):
        self.driver.get('https://www.newegg.com/RCA-Cables/SubCategory/ID-2831?cm_sp=Cat_Cables_3-_-VisNav-_-RCA-Cables_3')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="popup-close"]').click()
        time.sleep(1)
        arr = self.driver.find_elements_by_css_selector('.btn.btn-primary.btn-mini')
        while not arr:
            arr = self.driver.find_elements_by_css_selector('.btn.btn-primary.btn-mini')
            self.driver.refresh()
            time.sleep(10)
        arr[0].click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div/div/div[2]/div[2]/button[2]').click()

    def buyItem(self):
        wait = WebDriverWait(self.driver, 3)

        time.sleep(2)

        #self.driver.find_element_by_xpath('//*[@id="btnCreditCard"]').click()
        print("Purchased!")
