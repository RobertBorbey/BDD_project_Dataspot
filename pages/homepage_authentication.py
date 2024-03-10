from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class Homepage_authentication(Browser):
    AUTHENTICATION_BUTTON = (By.ID, 'user_info')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="login-form"]//input[@name = "email"]')
    PASSWORD = (By.XPATH, '//*[@id="login-form"]//*[@name = "password"]')
    SUBMIT_LOGIN = (By.XPATH, '//form[@id="login-form"]//button[contains(text(), "Intra in cont")]')
    ERROR_MESSAGE = (By.XPATH, '//section[@class="login-form"]//div[@class="help-block"]//ul//li')
    # MY_ACCOUNT_DROPDOWN = (By.XPATH, '//div[@class="col col-auto col-header-right text-right"]'
    #                                  '//div[@id="user_info"]//div[@class="dropdown"]')

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
            except Exception as i:
                logging.error(f"An error occurred while clicking the login button: {str(i)}")
            else:
                raise AssertionError("Login button element not found")
            attempts += 1

    def insert_email(self):
        try:
            wait = WebDriverWait(self.chrome,20)
            user_email_element = wait.until(
                EC.element_to_be_clickable((By.NAME, "email")))
            actions = ActionChains(self.chrome)
            actions.move_to_element(user_email_element).perform()
            user_email_element.click()
            user_email_element.send_keys("robertb.0629@gmail.com")
        except TimeoutException:
            print("Failed to load user email at www.dataspot.ro")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_invalid_password(self, password):
        try:
            wait = WebDriverWait(self.chrome,30)
            user_pass_element = wait.until(
                EC.element_to_be_clickable((By.NAME, "password")))
            actions = ActionChains(self.chrome)
            actions.move_to_element(user_pass_element).perform()
            user_pass_element.click()
            user_pass_element.send_keys(password)
        except TimeoutException:
            print("Failed to load user password at www.dataspot.ro")
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
            wait = WebDriverWait(self.chrome, 30)
            user_pass_element = wait.until(
                EC.element_to_be_clickable((By.NAME, "password")))
            actions = ActionChains(self.chrome)
            actions.move_to_element(user_pass_element).perform()
            user_pass_element.click()
            user_pass_element.send_keys("shoPPing0629")
        except TimeoutException:
            print("Failed to load user password at www.dataspot.ro")
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://dataspot.ro/"
        assert self.chrome.current_url == account_url
        logging.info("Test passed : Current URL matches the expected URL")

    def logout_page(self):
        try:
            my_account_button = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Contul meu')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(my_account_button).perform()
            my_account_button.click()
            logout_button = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Logout')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(logout_button).perform()
            logout_button.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the logout button : {str(i)}")

    def insert_invalid_email(self, email_address):
        try:
            invalid_email_element = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.NAME, "email")))
            actions = ActionChains(self.chrome)
            actions.move_to_element(invalid_email_element).perform()
            invalid_email_element.click()
            invalid_email_element.send_keys(email_address)
        except TimeoutException:
            print("Failed to load user password at www.dataspot.ro")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")

    def insert_my_email(self):
        try:
            my_email = self.chrome.find_element(*self.EMAIL_ADDRESS)
            my_email.clear()
            my_email.send_keys("robertb.0629@gmail.com")
        except Exception as i:
            logging.error(f"An error occurred while inserting the email : {str(i)}")
