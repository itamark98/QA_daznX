from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from gals_auto.accindazn import Menu, Login, Marco_polo
from staging import Stag


# class Stag:
# Create a Chrome browser object
driver = webdriver.Chrome()

# Go to the URL
driver.get("https://stag.dazn.com")

driver.maximize_window()
driver.implicitly_wait(10)

stge = Stag(driver)

stge.sign_in('gli@italy.com', '@kvgyj87i6@')
stge.search("")
sleep(1)
stge.schdule()
stge.get_into_event(9)
sleep(5)
driver.close()
