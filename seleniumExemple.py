from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chromedriver_path = r"D:\Driver\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5501/test.html")
time.sleep(2)
test = driver.find_elements(By.CLASS_NAME, "information")
# test.send_keys("admin@localhost.dev")
for i in test :
    i.send_keys("B")
    time.sleep(1)
    i.send_keys("o")
    time.sleep(1)
    i.send_keys("n")
    time.sleep(1)
    i.send_keys("j")
    time.sleep(1)
    i.send_keys("o")
    time.sleep(1)
    i.send_keys("u")
    time.sleep(1)
    i.send_keys("r")
    time.sleep(2)

driver.find_element(By.ID, "inputMale").click()
time.sleep(2)
driver.find_element(By.ID, "inputFemale").click()
time.sleep(100)