import time
from selenium.webdriver.chrome.options import Options
from Website import Website
from bs4 import BeautifulSoup
from selenium import webdriver
def main():
    test = "https://www.amazon.com/stores/page/26BBE2FD-3BC3-4057-9F6A-E7DCF1EB3838?ingress=0&visitId=f2837f71-4f84-49b5-a4f6-942d46887166"
    site = "https://www.amazon.com/stores/GeForce/RTX3080_GEFORCERTX30SERIES/page/6B204EA4-AAAC-4776-82B1-D7C3BD9DDC82"
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=C:\\Users\\cbass\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    driver = webdriver.Chrome(options=options)
    driver.get(site)
    time.sleep(5)
    arr = driver.find_elements_by_css_selector('button.style__addToCartBtn__nOP_z')
    while not arr:
        driver.refresh()
        arr = driver.find_elements_by_css_selector('button.style__addToCartBtn__nOP_z')
        time.sleep(60)
        print("No GPU")
    arr[0].click()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())
if __name__ == "__main__":
    main()
