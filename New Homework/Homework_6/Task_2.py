import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.freeconferencecall.com/login")

driver.delete_all_cookies()

COOKIES = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

for cookie in COOKIES:
    driver.add_cookie(cookie)

driver.get("https://www.freeconferencecall.com/profile")