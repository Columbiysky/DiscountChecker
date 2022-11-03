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
                EC.presence_of_element_located((By.CLASS_NAME, "_title_11f1r_2")))  # ждем
            priceElem = driver.find_element(
                By.CLASS_NAME, "_title_11f1r_2")
            oldPrice = self.numbersOnly(priceElem.find_element(
                By.XPATH, 'id("vue-root")/DIV[1]/MAIN[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]').text)
            currentPrice = self.numbersOnly(priceElem.find_element(
                By.XPATH,
                'id("vue-root")/DIV[1]/MAIN[1]/DIV[1]/DIV[2]/DIV[2]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[2]').text)
            if oldPrice in currentPrice:
                currentPrice = currentPrice.replace(oldPrice, '')
            print('True ' + currentPrice + ' '+oldPrice)
        except:
            locals_ = locals()
            if ('currentPrice' not in locals_ and 'oldPrice' in locals_):
                print('False ' + oldPrice)
            else:
                print(None)


if __name__ == '__main__':
    parser = DnsShopParse()
    parser.parse(sys.argv[1])
