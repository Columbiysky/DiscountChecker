import sys

from base import ParserBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BrandshopParse(ParserBase):
    def parse(self, link: str):
        driver = webdriver.Chrome()
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
            print('True ' + currentPrice + ' '+oldPrice)
        except:
            locals_ = locals()
            if ('oldPrice' not in locals_ and 'currentPrice' in locals_):
                print('False ' + currentPrice)
            elif ('priceWrapper' in locals_):
                print('False ' + self.numbersOnly(priceWrapper.text))
            else:
                print(None)


if __name__ == '__main__':
    parser = BrandshopParse()
    parser.parse('https://brandshop.ru/goods/369653/cu5506-010/')
    # mvidParser.parse(sys.argv[1])
