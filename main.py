from urllib.parse import urlparse

from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from selenium import webdriver

from parsers.parsersCollection import ParsersCollection

driver = webdriver.Chrome()
app = FastAPI()


@app.post("/")
def main(data=Body()):
    link = data["link"]
    domain = urlparse(link).hostname.replace('www.', '')
    parser = ParsersCollection.GetParser(domain)
    result = parser.parse(link, driver)
    return JSONResponse(result)
