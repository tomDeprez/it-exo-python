from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

chromedriver_path = r"D:\Driver\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://google.com")

time.sleep(2)
var = driver.find_element(By.CLASS_NAME, "spoKVd")
test = var.find_elements(By.TAG_NAME, "button")[1].click()
test.click()
time.sleep(2)
len()
bonjour = "bonjour"
bonjour.replace()