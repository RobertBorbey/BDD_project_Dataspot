from behave import *

@given("I am on the Dataspot website search results page and I want to sort the products by availability")
def step_impl(context):
    context.home_page.open_home_page()