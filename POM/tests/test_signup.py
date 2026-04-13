from pages.sign_up_page import SignUpPage
from pages.account_creation_page import Account_Creation
import random

email = f"vtusharkumar{random.randint(10,1000)}@gmail.com"


def test_full_signup(driver):
    signup = SignUpPage(driver)
    account = Account_Creation(driver)

    signup.load()
    signup.enter_name("Tushar")
    signup.enter_email(email)
    signup.click_login()

    assert "signup" in driver.current_url

    account.click_gender()
    account.enter_password("qwerty123")
    account.enter_day("12")
    account.enter_month("february")
    account.enter_year("2020")
    account.click_newsletter()
    account.click_optin()
    account.enter_fname("TusharV")
    account.enter_lname("kumar")
    account.enter_company("webyalaya")
    account.enter_address1("12/7 htype khamaria")
    account.enter_address2("none")
    account.enter_country("India")
    account.enter_state("MP")
    
    account.enter_city("jabalpur")
    account.enter_zipcode("49005")
    account.enter_mobile("9219312931")
    account.click_create_account()
    assert account.is_account_created()                           

   

    



