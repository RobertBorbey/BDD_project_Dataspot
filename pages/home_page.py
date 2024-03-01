from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
import logging

class Home_page(Browser):
    AUTHENTICATION_BUTTON = (By.ID, 'user_info')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="login-form"]//input[@name = "email"]')
    PASSWORD = (By.XPATH, '//*[@id="login-form"]//*[@name = "password"]')
    SUBMIT_LOGIN = (By.CSS_SELECTOR, '#login-form > footer>#submit-login')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#content > section > div > ul > li')

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
                    sleep(2)
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
            sleep(2)
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
            sleep(2)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password : {str(i)}")

    def click_sign_in_button(self):
        try:
            sign_in_button = self.chrome.find_element(*self.SUBMIT_LOGIN)
            sign_in_button.click()
            sleep(2)
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
            sleep(2)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://dataspot.ro/"
        assert self.chrome.current_url == account_url
        logging.info("Test passed : Current URL match the expected account URL")
        sleep(2)
