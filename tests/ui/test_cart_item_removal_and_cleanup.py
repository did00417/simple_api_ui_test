import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import BASE_URL
from pages.login_page import LoginPage

#3-1
def test_single_item_removal(driver):
    driver.get(BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.login()
    print("로그인 성공")
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    print("아이템 장바구니에 추가하기 클릭")
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_container").click()
    print("장바구니 아이콘 클릭")
    
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    print("장바구니 아이템 제거 클릭")
    
    time.sleep(5)  # 잠시 대기
    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0
    
    
# 3-2
def test_single_item_removal_with_fixture(app):
    app.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    print("아이템 장바구니에 추가하기 클릭")
    app.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("장바구니 아이콘 클릭")
    time.sleep(1)  # 잠시 대기
    app.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    print("장바구니 아이템 제거 클릭")
    time.sleep(1)  # 잠시 대기

    WebDriverWait(app, 5).until(
        lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == 0
    )
    print("장바구니 아이템이 제거될 때까지 대기")

    assert len(app.find_elements(By.CLASS_NAME, "cart_item")) == 0
    print("장바구니가 비어있는지 확인 검증 성공")

    