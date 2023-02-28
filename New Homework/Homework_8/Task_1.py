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
RADIO_BUTTON_MALE = ("xpath", "//input[@id='RESULT_RadioButton-7_0']")
RADIO_BUTTON_FEMALE = ("xpath", "//input[@id='RESULT_RadioButton-7_1']")
RADIO_BUTTON_FEMALE_LABEL = ("xpath", "//label[@for='RESULT_RadioButton-7_0']")

driver.switch_to.frame(IFRAME)
assert driver.find_element(*RADIO_BUTTON_MALE).is_enabled() is True, "Кнопка выбрана"

driver.find_element(*RADIO_BUTTON_FEMALE_LABEL).click()

assert driver.find_element(*RADIO_BUTTON_FEMALE).is_enabled(), "Кнопка не выбрана"
assert driver.find_element(*RADIO_BUTTON_MALE).is_enabled() is True, "Кнопка выбрана"