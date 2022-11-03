import sys

from base import ParserBase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YandexMarketParse(ParserBase):
    def parse(self, link: str):
        driver = webdriver.Chrome()
        driver.get(link)
        try:
            waitPage = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "KnVez")))  # ждем
            priceElem = driver.find_element(By.CLASS_NAME, "KnVez")
            newPrice = self.numbersOnly(priceElem.find_element(
                By.CSS_SELECTOR, "span[data-auto='mainPrice']").text)
            oldPrice = self.numbersOnly(priceElem.find_element(
                By.CLASS_NAME, "price__sale-value").text)
            print('True ' + newPrice + ' '+oldPrice)
        except:
            locals_ = locals()
            if ('elem2' not in locals_ and 'elem' in locals_):
                print('False ' + newPrice)
            print(None)


if __name__ == '__main__':
    mvidParser = YandexMarketParse()
    # mvidParser.parse(sys.argv[1])
    mvidParser.parse('https://market.yandex.ru/product--smartfon-apple-iphone-14-pro-max/1768738052?nid=34512430&show-uid=16674637884255687426716002&context=search&sku=101813096786&cpc=MOlNcyBeyLWoxloy9IIwypb6a2qqgagMHJwGzr94D2sBvfYBB9FZAqdBHy6w7BWZ8wkocwsnApZ5k0EMRTPmouu-8K621QNNUhVmLQdipVczq3R2uulSLU0eqKdmv9D62jAN6qNypNhkuL1BN0AJN3kUsMkweoBQ7-wRTi57fhy4GCDdbpqfRyHy7lucwaSHawiBv6Q9wG0%2C&do-waremd5=S5dF40uVhOVXQZxkHL9R7A&sponsored=1')
