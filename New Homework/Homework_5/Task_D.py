import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.set_window_size(1920,1080)
driver.get('https://demoqa.com/upload-download')

UPLOAD_FIELD = '//input[@type="file"]'

FILE_UPLOAD = driver.find_element(By.XPATH, UPLOAD_FIELD)
FILE_UPLOAD.send_keys("C:/Users/mstep/Desktop/mtn.jpeg")

time.sleep(2)
