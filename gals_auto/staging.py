from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class Stag:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def sign_in(self, email: str, password: str):
        self.driver.find_element(By.CLASS_NAME, 'css-1lo3n8p').click()
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        self.driver.find_element(By.ID, 'email').send_keys(email)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@class='sc-gKXOVf hxFrlM']").click()
        sleep(2)

# Option for the pages that in acc module
    def home(self):
        self.driver.find_element(By.XPATH, "//header//nav//ul[1]//li[@data-test-id='HEADER_LIST_ITEM'][1]").click()

    def schdule(self):
        self.driver.find_element(By.XPATH, "//header//nav//ul[1]//li[@data-test-id='HEADER_LIST_ITEM'][2]").click()

    def search(self, word: str):
        self.driver.find_element(By.XPATH, "//header//nav//ul[1]//li[@data-test-id='HEADER_LIST_ITEM'][6]").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[data-test-id='SEARCH_INPUT']").send_keys(word)

# Variable of int between 1-9 from up to down in the options of menu
    def menu(self, num: int):
        self.driver.find_element(By.XPATH, "//header//nav//ul[2]//li[@data-test-id='HEADER_LIST_ITEM']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, f"//header//nav//ul[2]//li[@data-test-id='HEADER_LIST_ITEM']//li"
                                           f"[{num}]//a").click()

# choose the number of the event you want, write it in the '[]' of the XPATH (count from left to right and op to do
    # wn in the Schedule place)
    def get_into_event(self, num: int):
        live = self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='WATCH_LIVE_BUTTON']")
        if live == 1:
            self.driver.find_element(By.XPATH, f"//section//ul//li[{num}]//a").send_keys(Keys.ARROW_DOWN)
            self.driver.find_element(By.XPATH, f"//section//ul//li[{num}]//a").click()
            return live.click
        else:
            self.driver.find_element(By.XPATH, f"//section//ul//li[{num}]//a").send_keys(Keys.ARROW_DOWN)
            self.driver.find_element(By.XPATH, f"//section//ul//li[{num}]//a").click()

        sleep(3)


class Party:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
