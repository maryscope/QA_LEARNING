import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#http://the-internet.herokuapp.com/download