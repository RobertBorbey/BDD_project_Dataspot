from browser import Browser
from pages.homepage_authentication import Homepage_authentication
from pages.homepage_registration import Homepage_registration
from pages.homepage_search_box import Homepage_search_box
from pages.homepage_sort_by import Homepage_sort_by

def before_all(context):
    context.browser = Browser()
    context.browser.maximize_windows()
    context.homepage_authentication = Homepage_authentication()
    context.homepage_registration = Homepage_registration()
    context.homepage_search_box = Homepage_search_box()
    context.homepage_sort_by = Homepage_sort_by()

def after_all(context):
    context.browser.close_browser()
