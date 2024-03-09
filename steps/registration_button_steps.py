from behave import *
from faker import Faker
fake = Faker()

@given("I am on the Dataspot homepage and I want to register with an invalid lastname and firstname")
def step_impl(context):
    context.homepage_registration.open_home_page()

@when("I click on the auth button")
def step_impl(context):
    context.homepage_registration.click_login_button()

@when("I click on the registration button")
def step_impl(context):
    context.homepage_registration.click_registration_button()

@when('I insert "{name_surname}" as the invalid name')
def step_impl(context, name_surname):
    context.homepage_registration.insert_firstname_lastname(name_surname)

@when("I enter a valid email address")
def step_impl(context):
    random_email = fake.email()
    context.homepage_registration.enter_random_email(random_email)

@when("I enter a random password")
def step_impl(context):
    context.homepage_registration.enter_password()

@when("I click on the create account button")
def step_impl(context):
    context.homepage_registration.create_account()

@then('"{error_name_msg}" is displayed')
def step_impl(context, error_name_msg):
    context.homepage_registration.registration_failed(error_name_msg)

@given("I am on the Dataspot homepage and I want to register with valid credentials")
def step_impl(context):
    context.homepage_registration.open_home_page()

@when("The authentication button is clicked")
def step_impl(context):
    context.homepage_registration.click_login_button()

@when("The registration button is selected")
def step_impl(context):
    context.homepage_registration.click_registration_button()

@when("I fill the first field with a valid name")
def step_impl(context):
    context.homepage_registration.valid_name()

@when("A random email address is entered")
def step_impl(context):
    random_email = fake.email()
    context.homepage_registration.enter_random_email(random_email)

@when("A password is entered")
def step_impl(context):
    context.homepage_registration.enter_password()

@when("I click the create account button")
def step_impl(context):
    context.homepage_registration.create_account()

@then("I am redirected back to the Dataspot homepage and the account was created succesfully")
def step_impl(context):
    context.homepage_registration.open_home_page()
