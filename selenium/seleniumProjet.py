from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chromedriver_path = r"D:\Driver\chromedriver.exe"# /!\
log_file = "selenium/log/log.txt"# /!\
url = "http://localhost/exoPHP/projet/form.php"# /!\
isDriver = True # /!\

if isDriver :
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
else :
    driver = webdriver.Chrome()

driver.get(url)

jeuDeTest = [
    ["", "", "", "", "", "", "", ""],
    ["Maria Garcia", "HealthCorp", "Nurse", "maria.garcia@healthcorp.com", "456 Health St", "Medicity", "Spain", "Madrid"],
    ["John Smith", "EduFuture", "Teacher", "john.smith@edufuture.com", "789 Education Rd", "Learnville", "United Kingdom", "London"],
    ["Liu Wei", "GreenEnergy", "Environmental Scientist", "liu.wei@greenenergy.com", "321 Eco Blvd", "EcoCity", "China", "Beijing"],
    ["Fatima Al Zahra", "ArtWorld", "Artist", "fatima.alzahra@artworld.com", "654 Art Ave", "CultureTown", "Morocco", "Casablanca"],
    ["Sven Eriksson", "AutoAdvance", "Mechanical Engineer", "sven.eriksson@autoadvance.com", "987 Auto Ln", "DriveCity", "Sweden", "Stockholm"],
    ["Chloe Dubois", "FashionForward", "Fashion Designer", "chloe.dubois@fashionforward.com", "213 Style St", "TrendyTown", "France", "Paris"],
    ["Raj Patel", "TechGiant", "Data Analyst", "raj.patel@techgiant.com", "654 Data Dr", "ComputeCity", "India", "Mumbai"],
    ["Anna Müller", "BuildBright", "Architect", "anna.muller@buildbright.com", "321 Design Rd", "Constructville", "Germany", "Berlin"],
    ["Pedro Alvarez", "FoodFiesta", "Chef", "pedro.alvarez@foodfiesta.com", "789 Gourmet Ave", "FlavorTown", "Mexico", "Mexico City"]
]

with open(log_file, 'w', encoding = "UTF-8") as file:
    file.write("")
for test in jeuDeTest :

    try:
        driver.find_element(By.ID, "firstName").send_keys(test[0])
        driver.find_element(By.ID, "lastName").send_keys(test[1])
        driver.find_element(By.ID, "username").send_keys(test[2])
        driver.find_element(By.ID, "email").send_keys(test[3])
        driver.find_element(By.ID, "address").send_keys(test[4])
        driver.find_element(By.ID, "address2").send_keys(test[5])
        country_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "country")))
        select = Select(country_dropdown)
        select.select_by_visible_text("United States")
        # # country_dropdown = driver.find_element_by_id("country")
        # # select = Select(country_dropdown)
        # # select.select_by_visible_text("United States")
        state_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "state")))
        select = Select(state_dropdown)
        select.select_by_visible_text("California")



        driver.find_element(By.ID, "zip").send_keys(test[6])

        driver.execute_script("document.getElementById('details').value='" + test[0] + "';")

        driver.find_element(By.ID, "same-address").click()
        driver.find_element(By.ID, "save-info").click()
        driver.find_element(By.ID, "debit").click()
        driver.find_element(By.ID, "cc-name").send_keys("avec un grand T")
        driver.find_element(By.ID, "cc-number").send_keys("0000 1234 9874 9510")
        driver.find_element(By.ID, "cc-name").send_keys(" comme Ta qua croire")
        driver.find_element(By.ID, "cc-expiration").send_keys("trop tard")
        driver.find_element(By.ID, "cc-cvv").send_keys("007")
        driver.find_element(By.ID, "checkoutForm").click()

        driver.get(url)


        time.sleep(2)
        # Écriture dans le fichier log
        with open(log_file, 'a', encoding = "UTF-8") as file:
            file.write(f'Test avec {test[0]} effectué à {time.ctime()} - Succès: test validé \n')

    except Exception as e:
        with open(log_file, 'a', encoding = "UTF-8") as file:
            file.write(f'Erreur lors du test avec {test[0]} à {time.ctime()} : test erreur\n')