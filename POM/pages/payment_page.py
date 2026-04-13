
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://automationexercise.com/payment"
        self.name_box = (By.NAME, "name_on_card")
        self.card_number = (By.NAME,"card_number")

        self.cvc = (By.NAME,"cvc")
        self.expiration_month = (By.NAME,"expiry_month")
        self.expiration_year = (By.NAME,"expiry_year")
        self.confirm_button = (By.ID,"submit")

    def enter_name(self,name):
        wait = WebDriverWait(self.driver,10)
        box = wait.until(EC.visibility_of_element_located(self.name_box))
        box.send_keys(name)

    def enter_card_number(self,num):
        self.driver.find_element(*self.card_number).send_keys(num)

    def enter_cvc(self,number):
        self.driver.find_element(*self.cvc).send_keys(number)

    def enter_expiry_month(self,month):
        self.driver.find_element(*self.expiration_month).send_keys(month)

    def enter_expiration_year(self,year):
        self.driver.find_element(*self.expiration_year).send_keys(year)

    def click_confirm_order(self):
        wait = WebDriverWait(self.driver,10)
        button = wait.until(element_to_be_clickable(self.confirm_button))
        button.click()

        

    


