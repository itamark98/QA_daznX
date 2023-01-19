from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Menu:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

# all the option for the pages that in acc module
    def my_profile(self):
        self.driver.find_element(By.CLASS_NAME, 'css-1dq9sam').click()

    def home(self):
        self.driver.find_element(By.XPATH, '//ul//li[1]').click()

    def marco_polo(self):
        self.driver.find_element(By.XPATH, '//ul//li[2]//div').click()

    def logout(self):
        self.driver.find_element(By.XPATH, '//ul//li[4]//div').click()
        self.driver.find_element(By.CLASS_NAME, 'css-1a94uj7-Button').click()

    def logoutcancel(self):
        self.driver.find_element(By.XPATH, '//ul//li[4]//div').click()
        sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'css-wtmugd-Button').click()


class Login:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def loginfrom_home(self):
        self.driver.find_element(By.CLASS_NAME, "css-mm7ba6-Button").click()
        self.driver.find_element(By.NAME, 'loginfmt').send_keys("gal.prager@ext.dazn.com")
        self.driver.find_element(By.ID, 'idSIButton9').click()
        self.driver.find_element(By.NAME, 'passwd').send_keys("@G!al12321")
        sleep(3)
        self.driver.find_element(By.ID, 'idSIButton9').click()
        sleep(20)
        self.driver.find_element(By.ID, 'idBtn_Back').click()
        sleep(8)

    def loginfrom_office(self):
        self.driver.find_element(By.CLASS_NAME, "css-mm7ba6-Button").click()
        self.driver.find_element(By.NAME, 'loginfmt').send_keys("gal.prager@ext.dazn.com")
        self.driver.find_element(By.ID, 'idSIButton9').click()
        self.driver.find_element(By.NAME, 'passwd').send_keys("@G!al12321")
        sleep(3)
        self.driver.find_element(By.ID, 'idSIButton9').click()
        sleep(3)
        self.driver.find_element(By.ID, 'idBtn_Back').click()
        sleep(4)


class Marco_polo:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_device(self):
        self.driver.get("https://www.dazn.com/en-IL/home")
        self.driver.find_element(By.XPATH, "//ul[2]//li[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='EMAIL']").send_keys("gal.prager@ext.dazn.com")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='PASSWORD']").send_keys("UMwTx8594&")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test-id='signIn__BUTTON']").click()
        # self.driver.find_element(By.LINK_TEXT, '/en-IL/search').click()
        self.driver.back()
        self.driver.back()
        self.driver.find_element(By.CLASS_NAME, "css-pscjdl-Button").click()
