import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(1920, 1080)
driver.get("https://demoqa.com/selectable")

GRID_TAB = ("xpath", "//a[@id='demo-tab-grid']")
ROW_2_ITEM = ("xpath", "//li[text() = 'Six']")
ROW_3_ITEM = ("xpath", "//li[text() = 'Seven']")

driver.find_element(*GRID_TAB).click()
time.sleep(3)

def click_item(row,cell):
    driver.find_element("xpath", f"//div[@class='list-group list-group-horizontal-sm'][{row}]//li[@class='list-group-item list-group-item-action'][{cell}]").click()

click_item(2,3)
click_item(3,1)

assert "active" in driver.find_element(*ROW_2_ITEM).get_attribute("class"), "Чек-бокс не выбран"
assert "active" in driver.find_element(*ROW_3_ITEM).get_attribute("class"), "Чек-бокс не выбран"

def unclick_item(cell):
    driver.find_element("xpath",f"//div[@class='list-group list-group-horizontal-sm']//li[@class='list-group-item active list-group-item-action'][text()='{cell}']").click()

unclick_item('Six')
unclick_item('Seven')
time.sleep(3)

assert " " in driver.find_element(*ROW_2_ITEM).get_attribute("class"), "Чек-бокс выбран"
assert " " in driver.find_element(*ROW_3_ITEM).get_attribute("class"), "Чек-бокс выбран"

# assert "active" in driver.find_element(*ROW_2_ITEM).get_attribute("class"), "Чек-бокс не выбран"
# assert "active" in driver.find_element(*ROW_3_ITEM).get_attribute("class"), "Чек-бокс не выбран"

