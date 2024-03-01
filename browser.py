from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging

class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()
    logging.basicConfig(level=logging.INFO)

    def maximize_windows(self):
        self.chrome.maximize_window()

    def close_browser(self):
        self.chrome.quit()