from selenium.webdriver.common.by import By
from steamtest.pages.base_page import BasePage

SEARCH_FIELD_LOCATOR_XPATH = "//input[contains(@id, 'store_nav_search_term')]"
SEARCH_BUTTON_LOCATOR_XPATH = "//a[contains(@id, 'store_search_link')]"

class HomePage(BasePage):
    def search_game(self, game_name):
        self.enter_text(By.XPATH, SEARCH_FIELD_LOCATOR_XPATH, game_name)
        self.submit_search(By.XPATH, SEARCH_BUTTON_LOCATOR_XPATH)



