#cart page

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://automationexercise.com/view_cart"

        self.product1name_loc = (By.XPATH, "//td[@class='cart_description']//a[text()='Blue Top']")
        self.product2name_loc = (By.XPATH, "//td[@class='cart_description']//a[text()='Men Tshirt']")
        self.removeprod1_button = (By.CSS_SELECTOR, "a.cart_quantity_delete[data-product-id='1']")
        self.removed_message = (By.XPATH, "//b[text()='Cart is empty!']")
        self.checkout_button = (By.XPATH, "//a[text()='Proceed To Checkout']")
        self.cart_quantity = (By.CLASS_NAME,"cart_quantity")

    def load(self):
        self.driver.get(self.url)

    def product1name(self):
        return self.driver.find_element(*self.product1name_loc).text

    def product2name(self):
        return self.driver.find_element(*self.product2name_loc).text

    def remove_product1(self):
        self.driver.find_element(*self.removeprod1_button).click()

    def is_cart_empty(self):
        wait = WebDriverWait(self.driver,10)
        message = wait.until(visibility_of_element_located(self.removed_message))
        return "Cart is empty!" in message.text

    def click_checkoutbutton(self):
        wait = WebDriverWait(self.driver,10)
        button = wait.until(EC.element_to_be_clickable(self.checkout_button))
        button.click()

    def click_continue_shopping(self):
        self.driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()

    def get_cart_quantity(self):
        return self.driver.find_element(*self.cart_quantity).text

    def is_checkout_button_present(self):
        return len(self.driver.find_elements(*self.checkout_button)) > 0


