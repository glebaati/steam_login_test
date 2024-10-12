import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def test_steam_login(driver):
    driver.get('https://store.steampowered.com/')
    driver.find_element(By.XPATH, "//a[contains(text(),'войти')]").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@type, 'text') and contains(@class, '_2GBWeup')]")))
    driver.find_element(By.XPATH, "//input[contains(@type, 'text') and contains(@class, '_2GBWeup')]").send_keys(random_string(10))
    driver.find_element(By.XPATH, "//input[contains(@type, 'password')]").send_keys(random_string(12))
    driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@disabled]")))
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//button[@disabled]")))
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Пожалуйста, проверьте')]")))
    assert "Пожалуйста, проверьте" in error_message.text

