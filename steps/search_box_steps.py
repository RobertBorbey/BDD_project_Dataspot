from behave import *

@given("I am on the Dataspot homepage and I want to search for a valid product")
def step_impl(context):
    context.home_page.open_home_page()

@when('I enter the "{product_name}" in the search box')
def step_impl(context, product_name):
    context.home_page.insert_valid_product(product_name)

@when("I click the search button")
def step_impl(context):
    context.home_page.click_search_button()

@then('I am redirected to a new page that contains the "{results_message}"')
def step_impl(context, results_message):
    context.home_page.listed_products(results_message)

@given("I am on the Dataspot homepage and I want to search for an invalid product")
def step_impl(context):
    context.home_page.open_home_page()

@when('I enter the "{invalid_product}" name in the search box')
def step_impl(context, invalid_product):
    context.home_page.insert_invalid_product(invalid_product)

@when("I click on the search button")
def step_impl(context):
    context.home_page.click_search_button()

@then('I am redirected to a new page with the following message displayed : "{no_results}"')
def step_impl(context, no_results):
    context.home_page.no_results_msg(no_results)

