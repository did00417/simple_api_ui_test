import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import BASE_URL


@pytest.mark.parametrize("accepted_username", [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
])
def test_login_success(driver, accepted_username):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys(accepted_username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 5).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url

def test_failed_login(driver):
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    
    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[data-test="error"]'))
    )
    assert "inventory.html" not in driver.current_url
    assert "Epic sadface" in error_msg.text  