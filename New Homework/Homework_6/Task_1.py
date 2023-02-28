import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(1920,1080)
driver.get("https://www.freeconferencecall.com/en/us")

SET_EMAIL = ('xpath', "//input[@id='main_email']")
SET_PASSWORD = ('xpath', "//input[@id='password']")
BUTTON = ('xpath', "//button[@id='signupbutton']")

EMAIL = driver.find_element(*SET_EMAIL).send_keys("mari_121@mail.com")
PASSWORD = driver.find_element(*SET_PASSWORD).send_keys("123")
BUTTON_ACTIVATE = driver.find_element(*BUTTON).click()
time.sleep(5)
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

time.sleep(5)




# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html