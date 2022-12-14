import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from parsers.base import ParserBase


class MvideoParse(ParserBase):
    def parse(self, link: str, driver: webdriver):
        driver.get(link)
        try:
            waitPage = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "mvid-primary-layout")))  # ждем
            priceElem = driver.find_element(By.TAG_NAME, "mvid-price")
            currentPrice = self.numbersOnly(priceElem.find_element(
                By.CLASS_NAME, "price__main-value").text)
            oldPrice = self.numbersOnly(priceElem.find_element(
                By.CLASS_NAME, "price__sale-value").text)
            return True, currentPrice, oldPrice
        except:
            locals_ = locals()
            if ('oldPrice' not in locals_ and 'currentPrice' in locals_):
                return False, currentPrice
            else:
                return None


if __name__ == '__main__':
    parser = MvideoParse()
    parser.parse(sys.argv[1])
