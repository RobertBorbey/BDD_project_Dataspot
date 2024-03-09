from behave import *

@given("I am on the Dataspot homepage and I want to authenticate with an invalid password")
def step_impl(context):
    context.homepage_authentication.open_home_page()

@when("I click on authentication button")
def step_impl(context):
    context.homepage_authentication.click_login_button()

@when("I enter the valid email address")
def step_impl(context):
    context.homepage_authentication.insert_email()

@when('I insert "{user_password}" as the invalid password')
def step_impl(context, user_password):
    context.homepage_authentication.insert_invalid_password(user_password)

@when("I click on sign in account button")
def step_impl(context):
    context.homepage_authentication.click_sign_in_button()

@then('I receive "{error_message}"')
def step_impl(context, error_message):
    context.homepage_authentication.login_failed(error_message)

@given("I am on the Dataspot homepage and I want to authenticate with an invalid email address")
def step_impl(context):
    context.homepage_authentication.open_home_page()

@when("I click on the authentication button")
def step_impl(context):
    context.homepage_authentication.click_sign_in_button()

@when('I enter "{email_address}" as the invalid email address')
def step_impl(context, email_address):
    context.homepage_authentication.insert_invalid_email(email_address)

@when("I insert my valid password")
def step_impl(context):
    context.homepage_authentication.insert_password()

@when("I click the sign in account button")
def step_impl(context):
    context.homepage_authentication.click_sign_in_button()

@then('I get "{error_msg}"')
def step_impl(context, error_msg):
    context.homepage_authentication.login_failed(error_msg)

@when("I enter my valid email address")
def step_impl(context):
    context.homepage_authentication.insert_my_email()

@when("I enter my valid password")
def step_impl(context):
    context.homepage_authentication.insert_password()

@when("I click on the sign in account button")
def step_impl(context):
    context.homepage_authentication.click_sign_in_button()

@when("I am redirected to the Dataspot homepage, while connected to my account")
def step_impl(context):
    context.homepage_authentication.my_account_page()

@then("I go to my account page and click the log out of my account button")
def step_impl(context):
    context.homepage_authentication.logout_page()
