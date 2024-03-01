from behave import *

@given("I am on the Dataspot homepage and I want to authenticate with an invalid password")
def step_impl(context):
    context.home_page.open_home_page()

@when("I click on authentication button")
def step_impl(context):
    context.home_page.click_login_button()

@when("I enter the valid email address")
def step_impl(context):
    context.home_page.insert_email()

@when('I insert my invalid "{user_password}"')
def step_impl(context, user_password):
    context.home_page.insert_invalid_password(user_password)

@when("I click on sign in account button")
def step_impl(context):
    context.home_page.click_sign_in_button()

@then('I receive an "{error_message}"')
def step_impl(context, error_message):
    context.home_page.login_failed(error_message)

@when("I enter my valid password")
def step_impl(context):
    context.home_page.insert_password()

@when("I click on the sign in account button")
def step_impl(context):
    context.home_page.click_sign_in_button()

@then("I am redirected to my account page")
def step_impl(context):
    context.home_page.my_account_page()
