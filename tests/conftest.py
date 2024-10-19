import pytest
from selenium import webdriver
class WebDriverSingleton:
    _driver = None
    @staticmethod
    def get_driver():
        if WebDriverSingleton._driver is None:
            WebDriverSingleton._driver = webdriver.Chrome()
            WebDriverSingleton._driver.maximize_window()
        return WebDriverSingleton._driver

    @staticmethod
    def quit_driver():
        if WebDriverSingleton._driver:
            WebDriverSingleton._driver.quit()
            WebDriverSingleton._driver = None

@pytest.fixture()
def driver(request):
    URL = 'https://store.steampowered.com/'
    driver = WebDriverSingleton.get_driver()
    param = request.param
    if param == 'ru':
        driver.get(URL + "?l=russian")
    elif param == 'en':
        driver.get(URL + "?l=english")
    yield driver
    WebDriverSingleton.quit_driver()
