import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome (service=service)

driver.set_window_size(1920,1080)

driver.get("https://www.freeconferencecall.com/en/us/login")

MAIL = '//input[@id="login_email"]'
PASSWORD = '//input[@id="password"]'
ENTER = '//button[@id="loginformsubmit"]'

LOGIN_PAGE_TITLE = driver.find_element(By.XPATH,'/html/head/title')

MAIL_ENTER = driver.find_element(By.XPATH,MAIL).send_keys('qa42@yandex.ru')

PASS_ENTER = driver.find_element(By.XPATH,PASSWORD).send_keys('123')

BUTTON = driver.find_element(By.XPATH,ENTER).click()
time.sleep(2)

PAGE_TITLE = driver.find_element(By.XPATH,'/html/head/title')

assert LOGIN_PAGE_TITLE != PAGE_TITLE
print('Успешный логин')


