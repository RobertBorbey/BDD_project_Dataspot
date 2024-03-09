from behave import *

@given("I am on the Dataspot homepage and I want to search for a valid product")
def step_impl(context):
    context.homepage_search_box.open_home_page()

@when('I enter "{product_name}" in the search box')
def step_impl(context, product_name):
    context.homepage_search_box.insert_valid_product(product_name)

@when("I click the search button")
def step_impl(context):
    context.homepage_search_box.click_search_button()

@then('I am redirected to a new page that contains "{results_message}"')
def step_impl(context, results_message):
    context.homepage_search_box.listed_products(results_message)

@given("I am on the Dataspot homepage and I want to search for an invalid product")
def step_impl(context):
    context.homepage_search_box.open_home_page()

@when('I enter "{invalid_product}" name in the search box')
def step_impl(context, invalid_product):
    context.homepage_search_box.insert_invalid_product(invalid_product)

@when("I click on the search button")
def step_impl(context):
    context.homepage_search_box.click_search_button()

@then('I am redirected to a new page with the following message displayed : "{no_results}"')
def step_impl(context, no_results):
    context.homepage_search_box.no_results_msg(no_results)

