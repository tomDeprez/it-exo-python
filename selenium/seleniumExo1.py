from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_test(driver, log_file, test_data):
    try:
        time.sleep(2)
        # Remplissage du formulaire
        driver.find_element(By.ID, 'nom').send_keys(test_data['nom'])
        time.sleep(2)
        driver.find_element(By.ID, 'prenom').send_keys(test_data['prenom'])
        time.sleep(2)
        driver.find_element(By.ID, 'age').send_keys(test_data['age'])
        time.sleep(2)
        driver.find_element(By.ID, 'dateNaissance').send_keys(test_data['dateNaissance'])
        time.sleep(2)
        driver.find_element(By.ID, 'dateNaissance').send_keys(Keys.RETURN)

        # Logique de test
        time.sleep(2)
        success = True

        # Écriture dans le fichier log
        with open(log_file, 'a') as file:
            file.write(f'Test avec {test_data} effectué à {time.ctime()} - Succès: {success}\n')

    except Exception as e:
        with open(log_file, 'a') as file:
            file.write(f'Erreur lors du test avec {test_data} à {time.ctime()} : {e}\n')


log_file = 'formulaire_test_log.txt'
chromedriver_path = r"D:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('http://127.0.0.1:5500/exo2.html')

# Données de test
tests = [
    {'nom': 'Doe', 'prenom': 'John', 'age': '30', 'dateNaissance': '01/01/1992'},
    {'nom': 'Smith', 'prenom': 'Jane', 'age': '25', 'dateNaissance': '05/05/1997'},
    {'nom': 'Brown', 'prenom': 'Emily', 'age': '22', 'dateNaissance': '10/10/2001'},
    {'nom': 'Johnson', 'prenom': 'Michael', 'age': '35', 'dateNaissance': '07/08/1988'},
    {'nom': 'Williams', 'prenom': 'Sarah', 'age': '28', 'dateNaissance': '12/12/1995'},
    {'nom': 'Jones', 'prenom': 'William', 'age': '40', 'dateNaissance': '15/03/1983'},
    {'nom': 'Garcia', 'prenom': 'Maria', 'age': '32', 'dateNaissance': '20/04/1991'},
    {'nom': 'Miller', 'prenom': 'David', 'age': '27', 'dateNaissance': '25/07/1996'},
    {'nom': 'Davis', 'prenom': 'Elizabeth', 'age': '29', 'dateNaissance': '30/01/1994'},
    {'nom': 'Rodriguez', 'prenom': 'Jose', 'age': '33', 'dateNaissance': '02/02/1990'},
    {'nom': 'Martinez', 'prenom': 'Carlos', 'age': '24', 'dateNaissance': '17/05/1999'},
    {'nom': 'Hernandez', 'prenom': 'Ana', 'age': '31', 'dateNaissance': '08/11/1992'},
    {'nom': 'Lopez', 'prenom': 'Miguel', 'age': '34', 'dateNaissance': '14/09/1989'},
    {'nom': 'Gonzalez', 'prenom': 'Luis', 'age': '36', 'dateNaissance': '21/06/1987'},
    {'nom': 'Wilson', 'prenom': 'George', 'age': '39', 'dateNaissance': '09/03/1984'},
    {'nom': 'Anderson', 'prenom': 'Robert', 'age': '37', 'dateNaissance': '13/07/1986'},
    {'nom': 'Thomas', 'prenom': 'Lisa', 'age': '26', 'dateNaissance': '18/08/1997'},
    {'nom': 'Taylor', 'prenom': 'Emma', 'age': '23', 'dateNaissance': '22/10/2000'},
    {'nom': 'Moore', 'prenom': 'Jake', 'age': '38', 'dateNaissance': '27/02/1985'},
    {'nom': 'Jackson', 'prenom': 'Sophia', 'age': '21', 'dateNaissance': '31/12/2002'}
]

# Exécution des tests en boucle
for test_data in tests:
    run_test(driver, log_file, test_data)

driver.quit()
