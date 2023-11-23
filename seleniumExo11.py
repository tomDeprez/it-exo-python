from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

chromedriver_path = r"D:\Driver\chromedriver.exe"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://google.com")
time.sleep(10)
driver.find_elements(By.CLASS_NAME, "sy4vM")[1].click()
time.sleep(10)
# Trouvez l'élément par sa classe, envoyez du texte et appuyez sur Entrée
driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Acheter un pull" + Keys.ENTER)

time.sleep(10)
driver.find_elements(By.CLASS_NAME, "GKS7s")[2].click()
time.sleep(10)
link = driver.find_element(By.CSS_SELECTOR, "a[jsname='UWckNb']")
link.click()
time.sleep(10)
driver.find_element(By.ID, "popin_tc_privacy_button_2").click()
time.sleep(100)