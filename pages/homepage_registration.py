from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from browser import Browser
import logging
from faker import Faker
fake = Faker()

class Homepage_registration(Browser):
    AUTHENTICATION_BUTTON = (By.ID, 'user_info')
    REGISTRATION_BUTTON = (By.CLASS_NAME, 'go-as-guest-arrow')
    FIRSTNAME_LASTNAME = (By.NAME, 'firstname')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    ERROR_NAME = (By.XPATH, '//*[@id="customer-form"]//div[2]//li')
    CREATE_BUTTON = (By.XPATH, '//*[@id="customer-form"]/footer/button')

    def open_home_page(self):
        self.chrome.get("https://dataspot.ro/")
        try:
            my_account_button = WebDriverWait(self.chrome, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Autentificare')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(my_account_button).perform()
            my_account_button.is_displayed()
        except Exception as i:
            logging.error(f"An error occurred while checking if the authentication button is available : {str(i)}")

    def click_login_button(self):
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.AUTHENTICATION_BUTTON)
                if login_button:
                    login_button.click()
                    break
                else:
                    raise AssertionError("Login button element not found")
            except Exception as i:
                logging.error(f"An error occurred while clicking the login button : {str(i)}")
                attempts += 1

    def click_registration_button(self):
        try:
            registration_button = self.chrome.find_element(*self.REGISTRATION_BUTTON)
            registration_button.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the registration button : {str(i)}")

    def insert_firstname_lastname(self, name_surname):
        try:
            firstname_and_lastname = self.chrome.find_element(*self.FIRSTNAME_LASTNAME)
            firstname_and_lastname.send_keys(name_surname)
        except Exception as i:
            logging.error(f"An error occurred while inserting the firstname and lastname : {str(i)}")

    def enter_password(self):
        try:
            random_password = self.chrome.find_element(*self.PASSWORD_INPUT)
            random_password.send_keys("Macarena321")
        except Exception as i:
            logging.error(f"An error occurred while inserting the password : {str(i)}")

    def registration_failed(self, error_name_msg):
        error_msg = self.chrome.find_element(*self.ERROR_NAME).text
        logging.info("Registration failed {}".format(error_msg))
        assert error_msg.strip() == error_name_msg.strip()

    def create_account(self):
        try:
            click_create = self.chrome.find_element(*self.CREATE_BUTTON)
            click_create.click()
        except Exception as i:
            logging.error(f"An error occurred while creating the new account : {str(i)}")

    def valid_name(self):
        try:
            v_name = self.chrome.find_element(*self.FIRSTNAME_LASTNAME)
            v_name.clear()
            v_name.send_keys("Abecede Eefgehas")
        except Exception as i:
            logging.error(f"An error occurred while inserting the firstname and lastname : {str(i)}")

    def enter_random_email(self, email):
        try:
            email_field = self.chrome.find_element(*self.EMAIL_INPUT)
            email_field.clear()
            email_field.send_keys(email)
        except Exception as e:
            logging.error(f"An error occurred while entering the email: {str(e)}")