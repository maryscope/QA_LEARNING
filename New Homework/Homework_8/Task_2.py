from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(1920, 1080)
driver.get("https://testautomationpractice.blogspot.com")

IFRAME = driver.find_element("xpath","//iframe")
CHECKBOX_MONDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_0']")
CHECKBOX_TUESDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_1']")
CHECKBOX_WEDNESDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_2']")
CHECKBOX_THURSDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_3']")
CHECKBOX_FRIDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_4']")
CHECKBOX_SATURDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_5']")
CHECKBOX_SUNDAY = ("xpath", "//input[@id='RESULT_CheckBox-8_6']")
CHECKBOX_WEDNESDAY_LABEL = ("xpath", "//label[@for='RESULT_CheckBox-8_2']")
CHECKBOX_SUNDAY_LABEL = ("xpath", "//label[@for='RESULT_CheckBox-8_6']")

driver.switch_to.frame(IFRAME)
assert driver.find_element(*CHECKBOX_MONDAY).is_enabled() is True, "Кнопка выбрана"
assert driver.find_element(*CHECKBOX_TUESDAY).is_enabled() is True, "Кнопка выбрана"
assert driver.find_element(*CHECKBOX_WEDNESDAY).is_enabled() is True, "Кнопка выбрана"
assert driver.find_element(*CHECKBOX_THURSDAY).is_enabled() is True, "Кнопка выбрана"
assert driver.find_element(*CHECKBOX_FRIDAY).is_enabled() is True, "Кнопка выбрана"
assert driver.find_element(*CHECKBOX_SATURDAY).is_enabled() is True, "Кнопка выбрана"
assert driver.find_element(*CHECKBOX_SUNDAY).is_enabled() is True, "Кнопка выбрана"

driver.find_element(*CHECKBOX_WEDNESDAY_LABEL).click()
driver.find_element(*CHECKBOX_SUNDAY_LABEL).click()

assert driver.find_element(*CHECKBOX_WEDNESDAY).is_enabled(), "Кнопка не выбрана"
assert driver.find_element(*CHECKBOX_SUNDAY).is_enabled(), "Кнопка не выбрана"