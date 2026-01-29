import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import BASE_URL
from pages.login_page import LoginPage

def test_add_to_cart(driver):
    driver.get(BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.login()
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-backpack"), "Remove"))
    assert "Remove" in driver.find_element(By.ID, "remove-sauce-labs-backpack").text
    
    driver.find_element(By.ID, "item_4_title_link").click()   
    assert "Remove" in driver.find_element(By.ID, "remove").text
    

