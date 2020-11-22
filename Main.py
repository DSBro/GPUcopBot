from Amazon import Amazon
from Zotac import Zotac
import time
def main():
    x = Zotac()
    while not x.any_in_stock():
        time.sleep(60)
if __name__ == "__main__":
    main()
