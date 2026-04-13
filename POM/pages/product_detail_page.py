from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetail:
    def __init__(self,driver):
        self.driver = driver
        self.driver.url = "https://automationexercise.com/product_details/1"
        self.driver.quantity_loc  = (By.ID,"quantity")
        self.add_to_cart_loc = (By.XPATH, "//button[normalize-space()='Add to cart']")
        self.continue_button_loc = (By.XPATH, "//button[text()='Continue Shopping']")
    
    def load(self):
        self.driver.get(self.driver.url)


    def update_product_quantity(self,num):
        box = self.driver.find_element(*self.driver.quantity_loc)
        box.clear()
        box.send_keys(num)

    def click_add_to_cart_button(self):
        self.driver.find_element(*self.add_to_cart_loc).click()

    def click_continue_button(self):
        wait = WebDriverWait(self.driver,10)
        button = wait.until(EC.visibility_of_element_located(self.continue_button_loc))
        button.click()

    
