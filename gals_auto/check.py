from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from gals_auto.accindazn import Menu, Login, Marco_polo


# Create a Chrome browser object
driver = webdriver.Chrome()

# Go to the URL
driver.get("https://acc.indazn.com/marco-polo")
driver.execute_script("window.open('https://www.dazn.com/en-IL/home')")

driver.maximize_window()
driver.implicitly_wait(10)

# objects:
menu = Menu(driver)
login = Login(driver)
marco = Marco_polo(driver)
################################
login.loginfrom_office()

menu.marco_polo()
sleep(2)

sleep(5)
marco.add_device()
sleep(5)
