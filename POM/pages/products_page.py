from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Productspage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://automationexercise.com/products"
        self.addproduct1_loc = (By.XPATH, "//a[@data-product-id='1']")
        self.continuebutton_loc = (By.XPATH, "//button[text()='Continue Shopping']")
        self.addproduct2_loc = (By.XPATH, "//a[@data-product-id='2']")
        self.search_box = (By.ID,"search_product")
        self.search_button = (By.ID,"submit_search")
        self.search_result_name = (By.XPATH, "//p[text()='Blue Top']")
        self.product_names = (By.XPATH, "//div[@class='productinfo text-center']//p")


    def load(self):
        self.driver.get(self.url)

    def addproduct1(self):
        wait = WebDriverWait(self.driver, 10)
        product = wait.until(EC.visibility_of_element_located(self.addproduct1_loc))
        actions = ActionChains(self.driver)
        actions.move_to_element(product).perform()
        
        button = wait.until(EC.element_to_be_clickable(self.addproduct1_loc))
        self.driver.execute_script("arguments[0].click();", button)

    def addproduct2(self):
        wait = WebDriverWait(self.driver, 10)
        product = wait.until(EC.visibility_of_element_located(self.addproduct2_loc))
        actions = ActionChains(self.driver)
        actions.move_to_element(product).perform()
        button = wait.until(EC.element_to_be_clickable(self.addproduct2_loc))
        self.driver.execute_script("arguments[0].click();", button)

    def continuebutton(self):
        wait = WebDriverWait(self.driver,10)
        
        button = wait.until(EC.element_to_be_clickable(self.continuebutton_loc))
        self.driver.execute_script("arguments[0].click();", button)

    def search_product(self, product_name):
         wait = WebDriverWait(self.driver, 10)
         box = wait.until(EC.visibility_of_element_located(self.search_box))
         box.send_keys(product_name)
         button = wait.until(EC.element_to_be_clickable(self.search_button))
         self.driver.execute_script("arguments[0].click();", button)

    def get_search_results(self):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(self.product_names))
        return [e.text for e in elements if e.text.strip() != ""]
         
         

   