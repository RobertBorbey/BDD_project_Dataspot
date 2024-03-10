from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from browser import Browser
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage_sort_by(Browser):
    PC_CATEGORY_BUTTON = (By.XPATH, '//nav[@id="cbp-hrmenu"]/ul/li/a')
    LAPTOP_BUTTON = (By.XPATH, '//div[@class="row"]/div/a')

    def open_home_page(self):
        self.chrome.get("https://dataspot.ro/")

    def select_pc_category(self):
        try:
            pc_button = self.chrome.find_element(*self.PC_CATEGORY_BUTTON)
            pc_button.click()
        except Exception as i:
            logging.error(f"An error occurred when selecting the 'Calculatoare' category dropdown button : {str(i)}")

    def pc_status(self):
        pc_url = "https://dataspot.ro/25-calculatoare"
        assert self.chrome.current_url == pc_url
        logging.info("Test passed : Current URL matches the expected URL")

    def select_laptop(self):
        try:
            laptop_button = self.chrome.find_element(*self.LAPTOP_BUTTON)
            laptop_button.click()
        except Exception as i:
            logging.error(f"An error occurred while selecting the 'Laptop' option : {str(i)}")

    def laptop_status(self):
        laptop_url = "https://dataspot.ro/26-laptop"
        try:
            assert self.chrome.current_url == laptop_url
            self.chrome.implicitly_wait(15)
            logging.info("Test passed: Current URL matches the expected URL")
        except Exception as i:
            logging.error(f"An error occurred: {str(i)}")

    def sort_dropdown(self):
        try:
            wait = WebDriverWait(self.chrome, 20)
            sort_button_element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="select-title expand-more form-control"]//i[@class="fas fa fa-angle-down"]')))
            sort_button_element.click()
            logging.info("Clicked on 'Sort' button")
        except Exception as i:
            logging.error(f"An error occurred while selecting the 'Sort By' dropdown : {str(i)}")

    def sort_by_availability(self):
        try:
            availability_button = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Disponibilitate')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(availability_button).perform()
            availability_button.click()
            button_text = availability_button.text.strip()
            logging.info(f"Clicked on '{button_text}' button")
        except Exception as i:
            logging.error(f"An error occurred when selecting the 'Disponibilitate' button from the dropdown : {str(i)}")

    def availability_status(self):
        availability_url = "https://dataspot.ro/26-laptop?order=stock.quantity.desc"
        try:
            WebDriverWait(self.chrome, 10).until(EC.url_to_be(availability_url))
            assert self.chrome.current_url == availability_url
            logging.info("Test passed: Current URL matches the expected URL")
        except Exception as i:
            logging.error(f"An error occurred: {str(i)}")

    def sort_by_ascending(self):
        try:
            ascending_button = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Pret - crescator')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(ascending_button).perform()
            ascending_button.click()
            button_text = ascending_button.text.strip()
            logging.info(f"Clicked on '{button_text}' button")
        except Exception as i:
            logging.error(f"An error occurred when selecting the 'Pret - crescator' button from the dropdown: {str(i)}")

    def ascending_status(self):
        ascending_url = "https://dataspot.ro/26-laptop?order=product.price.asc"
        try:
            WebDriverWait(self.chrome, 10).until(EC.url_to_be(ascending_url))
            assert self.chrome.current_url == ascending_url
            logging.info("Test passed: Current URL matches the expected URL")
        except Exception as i:
            logging.error(f"An error occurred: {str(i)}")

    def sort_by_descending(self):
        try:
            descending_button = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Pret - descrescator')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(descending_button).perform()
            descending_button.click()
            button_text = descending_button.text.strip()
            logging.info(f"Clicked on '{button_text}' button")
        except Exception as i:
            logging.error(f"An error occurred when selecting 'Pret - descrescator' button from the dropdown : {str(i)}")

    def descending_status(self):
        descending_url = "https://dataspot.ro/26-laptop?order=product.price.desc"
        try:
            WebDriverWait(self.chrome, 10).until(EC.url_to_be(descending_url))
            assert self.chrome.current_url == descending_url
            logging.info("Test passed: Current URL matches the expected URL")
        except Exception as i:
            logging.error(f"An error occurred: {str(i)}")

    def sort_by_newest_to_oldest(self):
        try:
            newest_button = WebDriverWait(self.chrome, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Cele mai noi')))
            actions = ActionChains(self.chrome)
            actions.move_to_element(newest_button).perform()
            newest_button.click()
            button_text = newest_button.text.strip()
            logging.info(f"Clicked on '{button_text}' button")
        except Exception as i:
            logging.error(f"An error occurred while selecting the 'Cele mai noi' button from the dropdown: {str(i)}")

    def newest_to_oldest_status(self):
        newest_url = "https://dataspot.ro/26-laptop?order=product.date_add.desc"
        try:
            WebDriverWait(self.chrome, 10).until(EC.url_to_be(newest_url))
            assert self.chrome.current_url == newest_url
            logging.info("Test passed: Current URL matches the expected URL")
        except Exception as i:
            logging.error(f"An error occurred: {str(i)}")
