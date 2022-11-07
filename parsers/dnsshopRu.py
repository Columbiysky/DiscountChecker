import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from parsers.base import ParserBase


class DnsShopParse(ParserBase):
    def parse(self, link: str, driver: webdriver):
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
            return True, currentPrice, oldPrice
        except:
            locals_ = locals()
            if ('oldPrice' not in locals_ and 'currentPrice' in locals_):
                return False, currentPrice
            else:
                return None


if __name__ == '__main__':
    parser = DnsShopParse()
    parser.parse(sys.argv[1])
