from selenium.webdriver.common.by import By
from browser import Browser
import logging
from time import sleep

class Homepage_sort_by(Browser):
    PC_CATEGORY_BUTTON = (By.XPATH, '//nav[@id="cbp-hrmenu"]/ul/li/a')
    LAPTOP_BUTTON = (By.XPATH, '//div[@class="row"]/div/a')
    DROPDOWN_BUTTON = (By.XPATH, '//a[@class="select-title expand-more form-control"]//i[@class="fas fa fa-angle-down"]')
    AVAILABILITY_BUTTON = (By.XPATH, '//div[@class="dropdown-menu show"]/a[1]')
    ASCENDING_BUTTON = (By.XPATH, '//div[@class="dropdown-menu show"]/a[2]')
    DESCENDING_BUTTON = (By.XPATH, '//div[@class="dropdown-menu show"]/a[3]')
    NEWEST_BUTTON = (By.XPATH, '//div[@class="dropdown-menu show"]/a[4]')

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
        assert self.chrome.current_url == laptop_url
        logging.info("Test passed : Current URL matches the expected URL")
        sleep(4)

    def sort_dropdown(self):
        try:
            sort_button = self.chrome.find_element(*self.DROPDOWN_BUTTON)
            sort_button.click()
            sleep(4)
        except Exception as i:
            logging.error(f"An error occurred while selecting the 'Sort By' dropdown : {str(i)}")

    def sort_by_availability(self):
        try:
            availability_button = self.chrome.find_element(*self.AVAILABILITY_BUTTON)
            availability_button.click()
            sleep(4)
        except Exception as i:
            logging.error(f"An error occurred when selecting the 'Disponibilitate' button from the dropdown : {str(i)}")

    def availability_status(self):
        availability_url = "https://dataspot.ro/26-laptop?order=stock.quantity.desc"
        assert self.chrome.current_url == availability_url
        logging.info("Test passed : Current URL matches the expected URL")

    def sort_by_ascending(self):
        try:
            ascending_button = self.chrome.find_element(*self.ASCENDING_BUTTON)
            ascending_button.click()
            sleep(4)
        except Exception as i:
            logging.error(f"An error occurred when selecting the 'Pret - crescator' button from the dropdown: {str(i)}")

    def ascending_status(self):
        ascending_url = "https://dataspot.ro/26-laptop?order=product.price.asc"
        assert self.chrome.current_url == ascending_url
        logging.info("Test passed : Current URL matches the expected URL")

    def sort_by_descending(self):
        try:
            descending_button = self.chrome.find_element(*self.DESCENDING_BUTTON)
            descending_button.click()
            sleep(4)
        except Exception as i:
            logging.error(f"An error occurred when selecting 'Pret - descrescator' button from the dropdown : {str(i)}")

    def descending_status(self):
        descending_url = "https://dataspot.ro/26-laptop?order=product.price.desc"
        assert self.chrome.current_url == descending_url
        logging.info("Test passed : Current URL matches the expected URL")

    def sort_by_newest_to_oldest(self):
        try:
            newest_button = self.chrome.find_element(*self.NEWEST_BUTTON)
            newest_button.click()
            sleep(4)
        except Exception as i:
            logging.error(f"An error occurred while selecting the 'Cele mai noi' button from the dropdown : {str(i)}")

    def newest_to_oldest_status(self):
        newest_url = "https://dataspot.ro/26-laptop?order=product.date_add.desc"
        assert self.chrome.current_url == newest_url
        logging.info("Test passed : Current URL matches the expected URL")
