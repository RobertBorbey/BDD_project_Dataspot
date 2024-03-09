from selenium.webdriver.common.by import By
from browser import Browser
import logging

class Homepage_search_box(Browser):
    SEARCH_BOX = (By.XPATH, '//*[@id="search_widget"]//input[@type="text"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search_widget"]//button[@class="search-btn"]')
    RESULTS_MSG = (By.XPATH, '//*[@id="wrapper"]/div/nav/div/div/ol/li/span')
    NO_PRODUCTS_MESSAGE = (By.XPATH, '//div[@id="content-wrapper"]//div[@role="alert"]')

    def open_home_page(self):
        self.chrome.get("https://dataspot.ro/")

    def insert_valid_product(self, product_name):
        try:
            name_of_product = self.chrome.find_element(*self.SEARCH_BOX)
            name_of_product.send_keys(product_name)
        except Exception as i:
            logging.error(f"An error occurred while inserting the product name : {str(i)}")

    def click_search_button(self):
        try:
            search_button = self.chrome.find_element(*self.SEARCH_BUTTON)
            search_button.click()
        except Exception as i:
            logging.error(f"An error occurred while clicking the search button : {str(i)}")

    def listed_products(self, expected_results):
        results_text = self.chrome.find_element(*self.RESULTS_MSG).text
        logging.info("Expected text: {}".format(results_text))
        assert results_text.strip() == expected_results.strip()

    def insert_invalid_product(self, invalid_product):
        try:
            name_of_invalid_product = self.chrome.find_element(*self.SEARCH_BOX)
            name_of_invalid_product.send_keys(invalid_product)
        except Exception as i:
            logging.error(f"An error occurred while inserting the invalid product name : {str(i)}")

    def no_results_msg(self, expected_no_results):
        no_results_alert = self.chrome.find_element(*self.NO_PRODUCTS_MESSAGE).text
        logging.info("Search result: {}".format(no_results_alert))
        assert no_results_alert.strip() == expected_no_results.strip()