from selenium.webdriver.common.by import By
class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/login"
        
        # Locators using By
        self.name_input = (By.NAME, "name")
        self.email_input = (By.CSS_SELECTOR, "[data-qa='signup-email']")
        self.signup = (By.CSS_SELECTOR, "[data-qa='signup-button']")

      # Error messages use h3 tag

    def load(self):
        print("[SignUpPage] Loading Automation Practice sign-up page...")
        self.driver.get(self.url)

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_login(self):
        self.driver.find_element(*self.signup).click()

    def get_error_message(self):
        return self.driver.find_element(
            By.XPATH, "//p[contains(text(),'Email Address already exist!')]"
        ).text

    





