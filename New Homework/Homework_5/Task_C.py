import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.set_window_size(1920,1080)
driver.get('http://the-internet.herokuapp.com/status_codes')

time.sleep(1)

LINK = '//a[contains(@href,"status_codes")]'
LINKS = driver.find_elements(By.XPATH, LINK)
print(LINKS)

for LINK in LINKS:
    LINK.click()
    time.sleep(2)
    driver.back()

time.sleep(2)
