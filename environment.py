from browser import Browser
from pages.home_page import Home_page
from pages.home_page_filter_sort import Home_page_filter_sort

def before_all(context):
    context.browser = Browser()
    context.browser.maximize_windows()
    context.home_page = Home_page()
    context.home_page_filter_sort = Home_page_filter_sort()

def after_all(context):
    context.browser.close_browser()
