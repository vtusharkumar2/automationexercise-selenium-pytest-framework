from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.address_text = (By.XPATH, "//h2[text()='Address Details']")
        self.name_loc = (By.XPATH, "//li[contains(@class,'address_firstname')]")
        self.address_loc = (By.XPATH, "(//li[contains(@class,'address_address1')])[2]")
        self.city_loc = (By.XPATH, "//li[contains(@class,'address_city')]")
        self.message_box = (By.NAME,"message")
        self.place_order = (By.XPATH, "//a[text()='Place Order']")
  



    def is_checkout_loaded(self):
        return self.driver.find_element(*self.address_text).is_displayed()

    def get_name(self):
        return self.driver.find_element(*self.name_loc).text

    def get_address_loc(self):
        return self.driver.find_element(*self.address_loc).text

    def get_city_loc(self):
        return self.driver.find_element(*self.city_loc).text

    def enter_message(self, message):
        box = self.driver.find_element(*self.message_box)
        self.driver.execute_script("arguments[0].scrollIntoView()", box)
        box.send_keys(message)

    def click_place_order(self):
        wait = WebDriverWait(self.driver,10)
        button = wait.until(EC.visibility_of_element_located(self.place_order))
        button.click()

        


