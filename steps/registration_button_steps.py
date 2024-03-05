from behave import *

@given("I am on the Dataspot homepage and I want to register with an invalid lastname and firstname")
def step_impl(context):
    context.home_page.open_home_page()

@when("I click on the auth button")
def step_impl(context):
    context.home_page.click_login_button()

@when("I click on the registration button")
def step_impl(context):
    context.home_page.click_registration_button()

@when('I insert an invalid "{name_surname}"')
def step_impl(context, name_surname):
    context.home_page.insert_firstname_lastname(name_surname)

@when("I enter a valid email address")
def step_impl(context):
    context.home_page.insert_valid_email()

@when("I enter a random password")
def step_impl(context):
    context.home_page.enter_password()

@when("I click on the create account button")
def step_impl(context):
    context.home_page.create_account()

@then('An "{error_name_msg}" is displayed')
def step_impl(context, error_name_msg):
    context.home_page.registration_failed(error_name_msg)

@when("The authentication button is clicked")
def step_impl(context):
    context.home_page.click_login_button()

@when("I fill the first field with a valid name")
def step_impl(context):
    context.home_page.valid_name()

@when("A valid email address is entered")
def step_impl(context):
    context.home_page.fill_random_email()

@when("I click the create account button")
def step_impl(context):
    context.home_page.create_account()

@then("I am redirected to the Dataspot homepage, while connected to my new account")
def step_impl(context):
    context.home_page.my_account_page()