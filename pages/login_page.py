from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from utils.constants import TEST_LOGIN_ID, TEST_LOGIN_PASSWORD
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys(TEST_LOGIN_ID)
        self.driver.find_element(By.ID, "password").send_keys(TEST_LOGIN_PASSWORD)
        self.driver.find_element(By.ID, "login-button").click()