from selenium.webdriver.common.by import By

class OrderPlaced:
    def __init__(self,driver):
        self.driver = driver
        self.order_confirm_msg = (By.XPATH, "//b[text()='Order Placed!']")
        self.continue_btn = (By.XPATH, "//a[@data-qa='continue-button']")



    def get_order_confirm_text(self):
        return self.driver.find_element(*self.order_confirm_msg).text

    def click_continue_button(self):
        self.driver.find_element(*self.continue_btn).click()