import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.set_window_size(1920,1080)
driver.get('https://hyperskill.org/tracks')
time.sleep(3)

#Header
MAIN_LOGO = '(//*[@title="JetBrains Academy"])[1]'
PRICING = '//a[1][text()=" Pricing "]'
JOIN_ORG = '//a[text()=" For Business "]'
JOIN_IND = '//a[text()=" Join as individual "]'
SIGN_IN = '//button[@class="btn btn-outline-light text-nowrap btn-sm"]'

#Body
ALL_TRACKS = '//a[text()=" All tracks "]'
All_ELEMENTS = '//a[@class="btn btn-category rounded-pill"]'
ALL_CARDS = '//div[@class="card-body"]'

#Footer
LOGO2 = '(//*[@title="JetBrains Academy"])[2]'
TRACKS = '//a[text()=" Tracks "]'
PRICING_2 = '//a[2][text()=" Pricing "]'
FOR_ORG = '//a[text()=" For organizations "]'
ABOUT = '//a[text()=" About "]'
CONTRIBUTE = '//a[text()=" Contribute "]'
CAREERS = '//a[text()=" Careers "]'
TERMS = '//a[text()=" Terms "]'
SUPPORT = '//a[text()=" Support "]'
REDDIT = '//*[@class="icon-reddit"]'
FACEBOOK = '//*[@class="icon-facebook"]'
MADE_WITH = '//*[@class="hs-love sm-expand"]'


driver.find_element(By.XPATH,MAIN_LOGO)
print("Main logo")
# driver.find_element(By.XPATH,PRICING)
# print("Pricing")
# driver.find_element(By.XPATH,JOIN_ORG)
# print("ORG Join")
# driver.find_element(By.XPATH,JOIN_IND)
# print("IND Join")
# driver.find_element(By.XPATH,SIGN_IN)
# print("SIGN IN")
# time.sleep(1)
#
# driver.find_element(By.XPATH,ALL_TRACKS)
# print("All Tracks")
# All_ELEMENTS_SRCH = driver.find_elements(By.XPATH, All_ELEMENTS)
# print(All_ELEMENTS_SRCH[3].text)
# All_CARDS_SRCH = driver.find_elements(By.XPATH, ALL_CARDS)
# print(All_CARDS_SRCH[6].text)
# time.sleep(1)
#
# driver.find_element(By.XPATH,LOGO2)
# print("Logo2")
# driver.find_element(By.XPATH,TRACKS)
# print("Tracks")
# driver.find_element(By.XPATH,PRICING_2)
# print("Pricing2")
# driver.find_element(By.XPATH,FOR_ORG)
# print("For Org")
# driver.find_element(By.XPATH,ABOUT)
# print("About")
# driver.find_element(By.XPATH,CONTRIBUTE)
# print("Contribute")
# driver.find_element(By.XPATH,CAREERS)
# print("Careers")
# driver.find_element(By.XPATH,TERMS)
# print("Terms")
# driver.find_element(By.XPATH,SUPPORT)
# print("Support")
# driver.find_element(By.XPATH,REDDIT)
# print("Reddit icon")
# driver.find_element(By.XPATH,FACEBOOK)
# print("Facebook icon")
# driver.find_element(By.XPATH,MADE_WITH)
# print("Made with love")

