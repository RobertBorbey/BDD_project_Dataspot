from selenium.webdriver.common.by import By
from browser import Browser
import logging
from faker import Faker

fake = Faker()

class Home_page(Browser):
    AUTHENTICATION_BUTTON = (By.ID, 'user_info')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="login-form"]//input[@name = "email"]')
    PASSWORD = (By.XPATH, '//*[@id="login-form"]//*[@name = "password"]')
    SUBMIT_LOGIN = (By.XPATH, '//*[@id="login-form"]//button[@id="submit-login"]')
    ERROR_MESSAGE = (By.XPATH, '//section[@class="login-form"]//div[@class="help-block"]//ul//li')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/div[1]/a[8]')
    REGISTRATION_BUTTON = (By.CLASS_NAME, 'go-as-guest-arrow')
    FIRSTNAME_LASTNAME = (By.NAME, 'firstname')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    ERROR_NAME = (By.XPATH, '//*[@id="customer-form"]//div[2]//li')
    CREATE_BUTTON = (By.XPATH, '//*[@id="customer-form"]/footer/button')

    def open_home_page(self):
        self.chrome.get("https://dataspot.ro/")

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

    def insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.EMAIL_ADDRESS)
            user_email.send_keys("rob")
            user_email.send_keys("ert")
            user_email.send_keys("b.")
            user_email.send_keys("06")
            user_email.send_keys("29")
            user_email.send_keys("@gm")
            user_email.send_keys("ail")
            user_email.send_keys(".com")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password : {str(i)}")

    def click_sign_in_button(self):
        try:
            sign_in_button = self.chrome.find_element(*self.SUBMIT_LOGIN)
            sign_in_button.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the SIGN IN button : {str(i)}")

    def login_failed(self, expected_error_message):
        error_text = self.chrome.find_element(*self.ERROR_MESSAGE).text
        logging.info("Login failed {}".format(error_text))
        assert error_text.strip() == expected_error_message.strip()

    def insert_password(self):
        try:
            user_pass = self.chrome.find_element(*self.PASSWORD)
            user_pass.send_keys("s")
            user_pass.send_keys("h")
            user_pass.send_keys("o")
            user_pass.send_keys("P")
            user_pass.send_keys("P")
            user_pass.send_keys("i")
            user_pass.send_keys("n")
            user_pass.send_keys("g")
            user_pass.send_keys("0")
            user_pass.send_keys("6")
            user_pass.send_keys("2")
            user_pass.send_keys("9")
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://dataspot.ro/"
        assert self.chrome.current_url == account_url
        logging.info("Test passed : Current URL match the expected account URL")

    def logout_page(self):
        self.chrome.get("https://dataspot.ro/identitate")
        try:
            logout_push = self.chrome.find_element(*self.LOGOUT_BUTTON)
            logout_push.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the logout button : {str(i)}")

    def insert_invalid_email(self, email_address):
        try:
            invalid_email = self.chrome.find_element(*self.EMAIL_ADDRESS)
            invalid_email.send_keys(email_address)
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_my_email(self):
        try:
            my_email = self.chrome.find_element(*self.EMAIL_ADDRESS)
            my_email.clear()
            my_email.send_keys("robertb.0629@gmail.com")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

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
            logging.error(f"An error occurred while inserting the valid password : {str(i)}")

    def registration_failed(self, error_name_msg):
        error_msg = self.chrome.find_element(*self.ERROR_NAME).text
        logging.info("Login failed {}".format(error_msg))
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
            v_name.send_keys("Gheoghe Moldoveanu")
        except Exception as i:
            logging.error(f"An error occurred while inserting the valid name : {str(i)}")

    def enter_random_email(self, email):
        try:
            email_field = self.chrome.find_element(*self.EMAIL_INPUT)
            email_field.clear()
            email_field.send_keys(email)
        except Exception as e:
            logging.error(f"An error occurred while entering the email: {str(e)}")