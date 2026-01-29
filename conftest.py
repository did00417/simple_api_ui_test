import pytest
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from core.api.api_client import APIClient

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--incognito")
    
    # OS 확인 (Windows, Linux, Darwin 등)
    current_os = platform.system()
    
    # 리눅스(CI/서버) 환경인 경우에만 Headless 적용
    if current_os == "Linux":
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080') # Headless 시 요소 안보임 방지
        print(f"\n[INFO] Environment: {current_os} -> Running in Headless mode")
    
    # 윈도우나 맥(로컬 개발) 환경인 경우 GUI 모드
    else:
        # GUI 환경에서 최대화해서 요소가 안 보이는 걸 방지
        options.add_argument("--start-maximized")
        print(f"\n[INFO] Environment: {current_os} -> Running in GUI mode")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def api():
    return APIClient("https://jsonplaceholder.typicode.com")