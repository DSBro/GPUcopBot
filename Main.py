from Amazon import Amazon
from Newegg import Newegg
def main():
    x = Amazon()
    x.login()
    x.checkStock()
    x.buyItem()
if __name__ == "__main__":
    main()
