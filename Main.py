import time
from Amazon import Amazon
from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    x = Amazon()
    x.checkStock()
    x.buyItem()
if __name__ == "__main__":
    main()
