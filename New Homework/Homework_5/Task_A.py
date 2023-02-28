import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.set_window_size(1920,1080)
driver.get('https://demoqa.com/text-box')


FULL_NAME = '//input[@placeholder="Full Name"]'
EMAIL_FIELD = '//input[@placeholder="name@example.com"]'
CURRENT_ADDRESS = "//textarea[@placeholder='Current Address']"
PERMANENT_ADDRESS = '//textarea[@id="permanentAddress"]'
SUBMIT_BUTTON = '//button[text()="Submit"]'

FULLNAME = driver.find_element(By.XPATH, FULL_NAME)
FULLNAME.clear()
FULLNAME.send_keys("Marina")
assert FULLNAME.get_attribute("value") == "Marina", "Данные введены неверно"

EMAIL = driver.find_element(By.XPATH, EMAIL_FIELD)
EMAIL.clear()
EMAIL.send_keys("marina@somemail.com")
assert EMAIL.get_attribute("value") == "marina@somemail.com", "Данные введены неверно"

CA_FIELD = driver.find_element(By.XPATH, CURRENT_ADDRESS)
CA_FIELD.clear()
CA_FIELD.send_keys("Bishkek")
assert CA_FIELD.get_attribute("value") == "Bishkek", "Данные введены неверно"

PA_FIELD = driver.find_element(By.XPATH, PERMANENT_ADDRESS)
PA_FIELD.clear()
PA_FIELD.send_keys("Turkey")
assert PA_FIELD.get_attribute("value") == "Turkey", "Данные введены неверно"

driver.find_element(By.XPATH, SUBMIT_BUTTON).click


time.sleep(3)
