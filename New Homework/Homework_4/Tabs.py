import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.set_window_size(1920,1080)
driver.get('https://hyperskill.org/login')
FIRST_TAB = driver.current_window_handle
print("первое окно", FIRST_TAB)

driver.switch_to.new_window("tab")
driver.get('https://www.avito.ru/')
SECOND_TAB = driver.current_window_handle
print("второе окно", SECOND_TAB)

driver.switch_to.new_window("tab")
driver.get('https://www.ozon.ru/')
THIRD_TAB = driver.current_window_handle
print("третье окно", THIRD_TAB)

driver.switch_to.window(FIRST_TAB)
print(driver.title)
driver.switch_to.window(SECOND_TAB)
print(driver.title)
driver.switch_to.window(THIRD_TAB)
print(driver.title)

HYPERSKILL_LINK ='//a[text()=" For Business "]'
AVITO_LINK = '//a[text()="Помощь"]'
OZON_LINK = '//*[text()="Заказы"]'

driver.switch_to.window(FIRST_TAB)
driver.find_element(By.XPATH, HYPERSKILL_LINK).click()
print("Hyperskill link opened")

driver.switch_to.window(SECOND_TAB)
driver.find_element(By.XPATH, AVITO_LINK).click()
print("Avito link opened")

driver.switch_to.window(THIRD_TAB)
driver.find_element(By.XPATH, OZON_LINK).click()
print("Ozon link opened")

