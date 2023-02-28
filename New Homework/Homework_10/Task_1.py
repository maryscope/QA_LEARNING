import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

driver.set_window_size(1920, 1080)

# Универсальная функция для метода click(), с включенный в нее ожиданием кликабельности
driver.get("https://demoqa.com/dynamic-properties")

FIRST_BUTTON = ("xpath", "//button[@id='enableAfter']")
COLOR_BUTTON = ("xpath", "//button[@id='colorChange']")
HIDDEN_BUTTON = ("xpath", "//button[@id='visibleAfter']")

def wait_and_click(element):
    wait.until(EC.element_to_be_clickable(element))
    driver.find_element(*element).click()
    print("Button pressed")

wait_and_click(FIRST_BUTTON)
wait_and_click(COLOR_BUTTON)
wait_and_click(HIDDEN_BUTTON)

# Универсальная функция для поиска элемента, с включенным в нее ожиданием появления элемента
driver.get('https://hyperskill.org/tracks')
def find_element(element):
    wait.until(EC.presence_of_element_located(("xpath", f"//a[@click-event-target='category'][{element}]")))
    ELEMENT = driver.find_element("xpath", f"//a[@click-event-target='category'][{element}]")
    print(ELEMENT.text)
    ELEMENT.click()

find_element('4')

# Универсальная функция для ввода данных в поле ввода, с проверкой результата ввода
driver.get("https://testautomationpractice.blogspot.com")

IFRAME = driver.find_element("xpath","//iframe")

driver.switch_to.frame(IFRAME)

def text_input(postion, text):
    EMPTY_FIELD = driver.find_element("xpath", f"//input[@name='RESULT_TextField-{postion}']")
    EMPTY_FIELD.send_keys(f"{text}")
    TEXT_VALUE = EMPTY_FIELD.get_attribute("value")
    print(TEXT_VALUE)
    assert TEXT_VALUE != EMPTY_FIELD, "Пусто"

text_input(1,"Marina")

# Универсальная функция для работы с чек-боксами и радио-кнопкам

driver.get("https://testautomationpractice.blogspot.com")

IFRAME = driver.find_element("xpath","//iframe")
RADIO_BUTTON_FEMALE_LABEL = ("xpath", "//label[@for='RESULT_RadioButton-7_1']")
RADIO_BUTTON_MALE = ("xpath", "//input[@id='RESULT_RadioButton-7_0']")
RADIO_BUTTON_FEMALE = ("xpath", "//input[@id='RESULT_RadioButton-7_1']")

driver.switch_to.frame(IFRAME)

def radiobutton_click(position):
    driver.find_element("xpath", f"//label[@for='RESULT_RadioButton-7_{position}']").click()

radiobutton_click(1)

def day_choose(day):
    driver.find_element("xpath", f"//label[@for='RESULT_CheckBox-8_{day}']").click()

day_choose(2)
day_choose(3)
day_choose(5)

time.sleep(3)

# Универсальная функция для загрузки файлов на сайт

driver.get("https://demoqa.com/upload-download")
UPLOAD_BUTTON = ('xpath', "//input[@id='uploadFile']")

def input_file(filename):
    driver.find_element(*UPLOAD_BUTTON).send_keys(os.getcwd() + f"{filename}")

input_file("\logo.jpg")

time.sleep(3)

# Универсальная функция для сохранения куков

driver.get("https://www.freeconferencecall.com/en/us")

SET_EMAIL = ('xpath', "//input[@id='main_email']")
SET_PASSWORD = ('xpath', "//input[@id='password']")
BUTTON = ('xpath', "//button[@id='signupbutton']")

def save_cookies(email, password,filename):
    driver.find_element(*SET_EMAIL).send_keys(f"{email}")
    driver.find_element(*SET_PASSWORD).send_keys(f"{password}")
    driver.find_element(*BUTTON).click()
    pickle.dump(driver.get_cookies(), open(os.getcwd() + f"/Cookies/{filename}", "wb"))

save_cookies('maristep122@mail.com', '1234', "newcookies.pkl")


# Универсальная функция для постановки куков из файла
driver.get("https://www.freeconferencecall.com/login")
driver.delete_all_cookies()
def upload_cookie(filename):
    COOKIES = pickle.load(open(os.getcwd()+f"/Cookies/{filename}", "rb"))
    for cookie in COOKIES:
        driver.add_cookie(cookie)
    driver.get("https://www.freeconferencecall.com/profile")

upload_cookie("newcookies.pkl")

driver.get("https://www.freeconferencecall.com/profile/account-info-login")


