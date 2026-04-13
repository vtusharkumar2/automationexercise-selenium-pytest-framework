from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.email = (By.NAME,"email")
        self.password = (By.NAME,"password")
        self.login_button = (By.CSS_SELECTOR, "[data-qa='login-button']")
    
    def load(self):
        self.driver.get("https://automationexercise.com/login")

    def enter_email(self,email):
        logger.info(f"Entering email: {email}")
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        logger.info("Clicking login button")
        self.driver.find_element(*self.login_button).click()

    def get_logged_in_text(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").text

    def get_error_message(self):
        return self.driver.find_element(
            By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]"
        ).text