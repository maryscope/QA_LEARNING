import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
preference = {
    "download.default_directory": os.getcwd() + "\downloads",
 }
options.add_experimental_option("prefs", preference)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(1920,1080)
driver.get('http://the-internet.herokuapp.com/download')

DOWNLOAD_LINK = '//a[text()]'
LINKS = driver.find_elements(By.XPATH,DOWNLOAD_LINK)

for DOWNLOAD_LINK in LINKS:
    DOWNLOAD_LINK.click()

time.sleep(5)