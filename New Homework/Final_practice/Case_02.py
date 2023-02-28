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
PASSWORD = driver.find_element(By.XPATH,PASS).send_keys('123')

BUTTON = driver.find_element(By.XPATH,BUTTON).click()
time.sleep(3)

ANONYM = '//span[@class="full-name"]'
PROFILE_ENTER = '//a[@title="My profile settings"]'

BUTTON_ANONYM = driver.find_element(By.XPATH,ANONYM).click()
time.sleep(4)
ENTER_PROFILE = driver.find_element(By.XPATH,PROFILE_ENTER).click()
time.sleep(3)

PHOTO = '//button[@class="photo-veil"]'
UPLOAD_FILE = "//input[@type='file']"
CLOSE_BUTTON = '//button[@name="apply_avatar_btn"]'
SAVE = '//button[@title="Save Changes"]'

PHOTO_CLICK = driver.find_element(By.XPATH,PHOTO).click()
PHOTO_UPLOAD = driver.find_element(By.XPATH, UPLOAD_FILE).send_keys("C:/Users/mstep/Desktop/mtn.jpeg")
time.sleep(5)
CLOSE_CLICK = driver.find_element(By.XPATH,CLOSE_BUTTON).click()
CLOSE_CLICK = driver.find_element(By.XPATH,SAVE).click()

time.sleep(5)



