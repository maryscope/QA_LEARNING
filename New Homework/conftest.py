# import pytest
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @pytest.fixture(scope="function", autouse=True)
# def connect_driver(request):
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     request.cls.wait = WebDriverWait(driver, 10, poll_frequency=1)
#     request.cls.driver = driver
#     yield
#     print("Куки успешно удалены")
#     driver.delete_all_cookies()
#     driver.quit()