import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string
STEAM_URL = "https://store.steampowered.com/"
TIMEOUT = 10

LOGIN_BUTTON_XPATH = "//a[contains(text(),'войти')]"
LOGIN_FIELD_XPATH = "//input[not(@type='password')]"
PASSWORD_FIELD_XPATH = "//input[contains(@type, 'password')]"
SUBMIT_BUTTON_XPATH = "//button[contains(@type, 'submit')]"
ERROR_MESSAGE_XPATH = "//form//div[5]"
LOADING_SIGN_XPATH = "//button[@disabled]"
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(STEAM_URL)
    yield driver

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def test_steam_login(driver):
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_XPATH))).click()
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, LOGIN_FIELD_XPATH))).send_keys(random_string(10))
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, PASSWORD_FIELD_XPATH))).send_keys(random_string(10))
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, SUBMIT_BUTTON_XPATH))).click()
    WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, LOADING_SIGN_XPATH)))
    WebDriverWait(driver, TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_SIGN_XPATH)))
    error_message = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, ERROR_MESSAGE_XPATH)))
    expected_message = "Пожалуйста, проверьте"
    actual_message = error_message.text
    assert expected_message in actual_message, (f"Failed: Expected message: '{expected_message}', "
        f"but got: '{actual_message}'")

