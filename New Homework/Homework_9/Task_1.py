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
RADIO_BUTTON_FEMALE_LABEL = ("xpath", "//label[@for='RESULT_RadioButton-7_1']")
BEST_TIME_DROPDOWN = ("xpath", "//select[@name='RESULT_RadioButton-9']")
FILE_UPLOAD = ("xpath", "//input[@name='RESULT_FileUpload-10']")
SUBMIT_BUTTON = ("xpath", "//input[@name='Submit']")

driver.switch_to.frame(IFRAME)
driver.find_element(*RADIO_BUTTON_FEMALE_LABEL).click()

def text_input(postion, text):
    driver.find_element("xpath", f"//input[@name='RESULT_TextField-{postion}']").send_keys(f'{text}')

text_input(1,"Marina")
text_input(2, "Ivanova")
text_input(3, "79219871234")
text_input(4, "Turkey")
text_input(5, "Antalya")
text_input(6, "m@yandex.ru")

def day_choose(day):
    driver.find_element("xpath", f"//label[@for='RESULT_CheckBox-8_{day}']").click()

day_choose(2)
day_choose(3)
day_choose(5)

driver.find_element(*BEST_TIME_DROPDOWN).send_keys("Mor")
# driver.find_element(*FILE_UPLOAD).send_keys(os.getcwd() + "\logo.jpg") #Загружает файл, но сайт выдает ошибку и все сбрасывается
driver.find_element(*SUBMIT_BUTTON).click() #Кнопка нажимается, но в итоге выдает ту же ошибку, что и при загрузке файла

