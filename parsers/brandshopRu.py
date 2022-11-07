import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from parsers.base import ParserBase


class BrandshopParse(ParserBase):
    def parse(self, link: str, driver: webdriver):
        driver.get(link)
        try:
            waitPage = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-order__price")))  # ждем
            priceElem = driver.find_element(
                By.CLASS_NAME, "product-order__price")
            priceWrapper = priceElem.find_element(
                By.CLASS_NAME, "product-order__price-wrapper")
            oldPrice = self.numbersOnly(priceWrapper.find_element(
                By.CLASS_NAME, "product-order__price_old").text)
            currentPrice = self.numbersOnly(priceElem.find_element(
                By.CLASS_NAME, "product-order__price_new").text)
            if oldPrice in currentPrice:
                currentPrice = currentPrice.replace(oldPrice, '')
            return True, currentPrice, oldPrice
        except:
            locals_ = locals()
            if ('oldPrice' not in locals_ and 'currentPrice' in locals_):
                return False, currentPrice
            elif ('priceWrapper' in locals_):
                return False, self.numbersOnly(priceWrapper.text)
            else:
                return None


if __name__ == '__main__':
    parser = BrandshopParse()
    parser.parse(sys.argv[1])
