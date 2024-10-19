from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, locator)))

    def find_elements(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((by, locator)))

    def click_element(self, by, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, locator))).click()

    def submit_search(self, by, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, locator))).submit()

    def enter_text(self, by, locator, text):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, locator))).send_keys(text)
