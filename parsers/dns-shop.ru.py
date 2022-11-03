import sys

from base import ParserBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DnsShopParse(ParserBase):
    def parse(self, link: str):
        driver = webdriver.Chrome()
        driver.get(link)
        try:
            waitPage = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-buy__price-wrap")))  # ждем
            priceElem = driver.find_element(
                By.CLASS_NAME, "product-buy__price-wrap")
            currentPrice = self.numbersOnly(priceElem.find_element(
                By.CLASS_NAME, "product-buy__price").text)
            oldPrice = self.numbersOnly(priceElem.find_element(
                By.CLASS_NAME, "product-buy__prev").text)
            if oldPrice in currentPrice:
                currentPrice = currentPrice.replace(oldPrice, '')
            print('True ' + currentPrice + ' '+oldPrice)
        except:
            locals_ = locals()
            if ('oldPrice' not in locals_ and 'currentPrice' in locals_):
                print('False ' + currentPrice)
            else:
                print(None)


if __name__ == '__main__':
    mvidParser = DnsShopParse()
    mvidParser.parse(sys.argv[1])
