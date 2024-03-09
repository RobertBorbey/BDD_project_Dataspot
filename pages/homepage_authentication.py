from selenium.webdriver.common.by import By
from browser import Browser
import logging

class Homepage_authentication(Browser):
    AUTHENTICATION_BUTTON = (By.ID, 'user_info')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="login-form"]//input[@name = "email"]')
    PASSWORD = (By.XPATH, '//*[@id="login-form"]//*[@name = "password"]')
    SUBMIT_LOGIN = (By.XPATH, '//*[@id="login-form"]//button[@id="submit-login"]')
    ERROR_MESSAGE = (By.XPATH, '//section[@class="login-form"]//div[@class="help-block"]//ul//li')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]//div[@class="row"]//div//a//span//i[@class="fa fa-sign-out fa-fw"]')

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
            user_email.send_keys("robertb.0629@gmail.com")
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
            user_pass.send_keys("shoPPing0629")
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://dataspot.ro/"
        assert self.chrome.current_url == account_url
        logging.info("Test passed : Current URL matches the expected URL")

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
