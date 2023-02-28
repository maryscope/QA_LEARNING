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
PASS = '//input[@id="password"]'
BUTTON = '//button[@id="loginformsubmit"]'

LOGIN = driver.find_element(By.XPATH,MAIL).send_keys('qa42@yandex.ru')
PASSWORD = driver.find_element(By.XPATH,PASS).send_keys('1234')

BUTTON = driver.find_element(By.XPATH,BUTTON).click()
time.sleep(3)

ANONYM = '//span[@class="full-name"]'
PROFILE_ENTER = '//a[@title="My profile settings"]'
EDIT_BUTTON = '//a[@name="edit_password"]'


BUTTON_ANONYM = driver.find_element(By.XPATH,ANONYM).click()
time.sleep(2)
ENTER_PROFILE = driver.find_element(By.XPATH,PROFILE_ENTER).click()
time.sleep(3)
EDIT_BUTTON = driver.find_element(By.XPATH, EDIT_BUTTON).click()
time.sleep(3)

CURRENT_PASS = '//input[@name="password"]'
NEW_PASS = '//input[@name="new_password"]'
CONFIRM_PASS = '//input[@name="password_confirmation"]'
CONFIRM_BUTTON = '//button[@name="btn_confirm"]'
LOGOUT_BUTTON = '//a[@title="Log Out"]'

OLDPASS = driver.find_element(By.XPATH,CURRENT_PASS).send_keys('1234')
NEWPASS = driver.find_element(By.XPATH,NEW_PASS).send_keys('123')
CONFIRMPASS = driver.find_element(By.XPATH,CONFIRM_PASS).send_keys('123')
CONFIRM = driver.find_element(By.XPATH,CONFIRM_BUTTON).click()
time.sleep(3)
BUTTON_ANONYM = driver.find_element(By.XPATH,ANONYM).click()
LOGOUT = driver.find_element(By.XPATH,LOGOUT_BUTTON).click()

time.sleep(2)
driver.switch_to.new_window()
driver.get("https://www.freeconferencecall.com/en/us/login")

LOGIN = driver.find_element(By.XPATH,MAIL).send_keys('qa42@yandex.ru')
PASSWORD = driver.find_element(By.XPATH,PASS).send_keys('123')
time.sleep(3)
BUTTON_RE = driver.find_element(By.XPATH,'//button[@id="loginformsubmit"]').click()
time.sleep(3)