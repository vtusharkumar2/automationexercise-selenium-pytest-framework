from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.logout_button = (By.XPATH,"//a[contains(text(),'Logout')]")
        self.url = "https://automationexercise.com/"


    def load(self):
        self.driver.get(self.url)



    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()