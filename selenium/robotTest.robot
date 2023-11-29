*** Settings ***
Documentation     Test de la page de paiement
Library           SeleniumLibrary

*** Variables ***
${URL}            http://localhost/exoPHP/projet/form.php
${BROWSER}        Chrome

*** Test Cases ***
Tester avec des données valides
    [Documentation]    Teste le formulaire avec des données valides.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    John    Doe    johndoe    johndoe@example.com    1234 Main St    12345    United States    California    John Doe    1234567890123456    12/23    123
    [Teardown]    Fermer le Navigateur
Tester avec des données de carte de crédit invalides
    [Documentation]    Teste le formulaire avec des données de carte de crédit invalides.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    Alice    Smith    alicesmith    alice@example.com    7890 Elm St    67890    United States    California    Alice Smith    0000111122223333    01/21    000
    [Teardown]    Fermer le Navigateur
Tester avec une adresse email invalide
    [Documentation]    Teste le formulaire avec une adresse e-mail invalide.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    Bob    Jones    bobjones    not-an-email    4567 Oak St    54321    United States    California    Bob Jones    1234567890123456    03/24    321
    [Teardown]    Fermer le Navigateur
Tester avec des champs obligatoires vides
    [Documentation]    Teste le formulaire avec certains champs obligatoires laissés vides.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    ''    ''    ''    user@example.com    ''    ''    United States    California    User Name    1234567890123456    05/26    123
    [Teardown]    Fermer le Navigateur
Tester avec des données excessivement longues
    [Documentation]    Teste le formulaire avec des données excessivement longues.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    LongFirstNameThatExceedsExpectedLength    LongLastNameThatExceedsExpectedLength    longusername    longemail@example.com    1234 Very Long Address Street That Exceeds Expected Length    12345    United States    California    Long Name on Card That Exceeds Expected Length    1234567890123456    12/30    999
    [Teardown]    Fermer le Navigateur
Tester avec des caractères spéciaux
    [Documentation]    Teste le formulaire avec des caractères spéciaux dans les champs de texte.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    Élise    O'Neil    élise.o'neil    elise@example.com    1234 Main St #5B    12345    United States    California    Élise O'Neil    1234567890123456    11/22    456
    [Teardown]    Fermer le Navigateur

Tester avec des données invalides
    [Documentation]    Teste le formulaire avec des données invalides.
    [Setup]    Ouvrir et Préparer la Page
    Remplir le Formulaire    ''    ''    ''    ''    ''    ''    ''    ''    ''    ''    ''    ''    ''
    [Teardown]    Fermer le Navigateur

*** Keywords ***
Ouvrir et Préparer la Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Open Browser    ${URL}    ${BROWSER}    options=${options}
    Maximize Browser Window
    Wait Until Page Contains    Checkout form    10s

Fermer le Navigateur
    Close Browser



*** Keywords ***
Remplir le Formulaire
    [Arguments]    ${firstName}    ${lastName}    ${username}    ${email}    ${address}    ${zip}    ${country}    ${state}    ${cc_name}    ${cc_number}    ${cc_expiration}    ${cc_cvv}
    # Remplir les champs de texte
    Input Text    id:firstName    ${firstName}
    Sleep    1s
    Input Text    id:lastName    ${lastName}
    Sleep    1s
    Input Text    id:username    ${username}
    Sleep    1s
    Input Text    id:email    ${email}
    Sleep    1s
    Input Text    id:address    ${address}
    Sleep    1s
    Input Text    id:zip    ${zip}
    Sleep    1s

    # Sélectionner les éléments des listes déroulantes
    Select From List By Label   id:country    United States  # Mettez à jour la valeur ici
    Sleep    1s
    Select From List By Label    id:state    California  # Mettez à jour la valeur ici
    Sleep    1s

    Input Text    id:details    test
    # Remplir les détails de paiement
    Input Text    id:cc-name    ${cc_name}
    Sleep    1s
    Input Text    id:cc-number    ${cc_number}
    Sleep    1s
    Input Text    id:cc-expiration    ${cc_expiration}
    Sleep    1s
    Input Text    id:cc-cvv    ${cc_cvv}
    Sleep    1s

    # Scroller jusqu'au bouton de soumission et cliquer
    Execute JavaScript    window.scrollTo(0, document.getElementById('checkoutForm').offsetTop)
    Sleep    2s
    Click Button    id:checkoutForm
    Sleep    2s
