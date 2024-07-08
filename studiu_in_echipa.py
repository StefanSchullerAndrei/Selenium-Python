import time   #ne ajuta sa folosim metoda sleep

from selenium import webdriver   # sa putem sa deschidem pagina web
from selenium.webdriver.common.by import By  #il folosim ca sa putem sa alegem tipul de selector *BY.CSS/BY.XPATH, ETC

driver = webdriver.Chrome() #deschide un Chrome
driver.maximize_window() #maximizam aplicatia
driver.get("https://www.elefant.ro/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
time.sleep(1)

#https://www.selenium.dev/documentation/webdriver/elements/locators/ documentatie

# driver.find_element(By.XPATH, '//input[@autocomplete="off" and @type="text"]').click()
# driver.find_element(By.XPATH, '//input[@autocomplete="off" and @type="text"]').send_keys("parfum")
# driver.find_element(By.XPATH, '//span[@class="glyphicon glyphicon-search"]').click()
# time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "a[title='Contact']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'div[class="o-btn o-btn-send"]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[class="o-input-field o-email-input"]').send_keys("nuareadresa@nu.avem")
time.sleep(1)
