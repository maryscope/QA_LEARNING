import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.set_window_size(1920,1080)
driver.get('https://demoqa.com/alerts')

CLICK_ME = '(//button[text()="Click me"])[3]'

#CONFIRM
SEARCH = driver.find_element(By.XPATH,CLICK_ME).click()
ALERT = driver.switch_to.alert
ALERT.accept()

time.sleep(3)

#DISMISS
SEARCH = driver.find_element(By.XPATH,CLICK_ME).click()
ALERT = driver.switch_to.alert
ALERT.dismiss()

time.sleep(3)