import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.jetbrains.com/")

time.sleep(1)
MAIN_TITLE = driver.title
print(MAIN_TITLE)

driver.get("https://www.cian.ru/")

time.sleep(1)

MAIN_TITLE2 = driver.title
print(MAIN_TITLE2)

driver.back()

MAIN_TITLE3 = driver.title
print(MAIN_TITLE3)
time.sleep(2)

assert MAIN_TITLE2 != MAIN_TITLE3
print('Вы вернулись на Jetbrains')

driver.refresh()
print('Обновлено')

URL = driver.current_url
print(URL)

driver.forward()

URL_NEW = driver.current_url
print(URL_NEW)

assert URL != URL_NEW
print('Вы открыли Cian')

time.sleep(1)