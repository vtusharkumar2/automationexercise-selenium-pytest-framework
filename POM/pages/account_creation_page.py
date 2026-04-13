import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Account_Creation:
    def __init__(self,driver):
        self.driver = driver
        self.gender = (By.ID,"id_gender1")
        self.password = (By.ID,"password")
        self.day = (By.ID,"days")
        self.month = (By.ID,"months")
        self.year = (By.ID,"years")
        self.newsletter = (By.ID,"newsletter")
        self.optin = (By.ID,"optin")
        self.fname = (By.ID,"first_name")
        self.lname = (By.ID,"last_name")
        self.company = (By.ID,"company")
        self.address1 = (By.ID,"address1")
        self.address2 = (By.ID,"address2")
        self.country = (By.ID,"country")
        self.state = (By.ID,"state")
        self.city = (By.ID,"city")
        self.zipcode = (By.ID,"zipcode")
        self.mobile = (By.ID,"mobile_number")
        self.create_account = (By.CSS_SELECTOR, "[data-qa='create-account']")
        self.create_account_success = (By.CSS_SELECTOR, "[data-qa='account-created']")


    def click_gender(self):
        self.driver.find_element(*self.gender).click()

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def enter_day(self,days):
        self.driver.find_element(*self.day).send_keys(days)

    def enter_month(self,month):
        self.driver.find_element(*self.month).send_keys(month)

    def enter_year(self,year):
        self.driver.find_element(*self.year).send_keys(year)

    def click_newsletter(self):
        self.driver.find_element(*self.newsletter).click()

    def click_optin(self):
        self.driver.find_element(*self.optin).click()

    def enter_fname(self,name):
        self.driver.find_element(*self.fname).send_keys(name)

    def enter_lname(self,lname):
        self.driver.find_element(*self.lname).send_keys(lname)

    def enter_company(self,companyn):
        self.driver.find_element(*self.company).send_keys(companyn)

    def enter_address1(self,address):
        self.driver.find_element(*self.address1).send_keys(address)

    def enter_address2(self,address2):
        self.driver.find_element(*self.address2).send_keys(address2)

    def enter_country(self,country_name):
        self.driver.find_element(*self.country).send_keys(country_name)

    def enter_state(self,state_name):
        self.driver.find_element(*self.state).send_keys(state_name)

    def enter_city(self,city_name):
        self.driver.find_element(*self.city).send_keys(city_name)

    def enter_zipcode(self,zipcode_input):
        self.driver.find_element(*self.zipcode).send_keys(zipcode_input)

    def enter_mobile(self,mobile_input):
        self.driver.find_element(*self.mobile).send_keys(mobile_input)

    def click_create_account(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_account)
            )
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    def is_account_created(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.create_account_success)
        )        


    

    
    
    
    


        
        
        

        