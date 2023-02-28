from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait (driver, 15)

driver.set_window_size(1920,1080)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

CHANGE_TEXT_BUTTON = ("xpath","//button[text()='Change Text to Selenium Webdriver']")
TEXT_CHANGE = ("xpath","//h2[@id='h2']")

driver.find_element(*CHANGE_TEXT_BUTTON).click()

wait.until(EC.text_to_be_present_in_element(TEXT_CHANGE, "Selenium Webdriver"))

