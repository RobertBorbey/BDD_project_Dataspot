from behave import *

@given("I am on the Dataspot website homepage, I want to see the laptops for sale and to sort them by availability")
def step_impl(context):
    context.homepage_sort_by.open_home_page()

@when("I click on the 'Calculatoare' category")
def step_impl(context):
    context.homepage_sort_by.select_pc_category()

@when("I am redirected to the selected category page")
def step_impl(context):
    context.homepage_sort_by.pc_status()

@when("I click on 'Laptop' option")
def step_impl(context):
    context.homepage_sort_by.select_laptop()

@when("I am redirected to the laptop products listed on the website")
def step_impl(context):
    context.homepage_sort_by.laptop_status()

@when("I select the Sort By dropdown")
def step_impl(context):
    context.homepage_sort_by.sort_dropdown()

@when("I click on the 'Disponibilitate' option")
def step_impl(context):
    context.homepage_sort_by.sort_by_availability()

@then("The products are sorted by availability")
def step_impl(context):
    context.homepage_sort_by.availability_status()

@when('I click on the "Pret - crescator" option')
def step_impl(context):
    context.homepage_sort_by.sort_by_ascending()

@then("The products are sorted by ascending price")
def step_impl(context):
    context.homepage_sort_by.ascending_status()

@when('I click on the "Pret - descrescator" option')
def step_impl(context):
    context.homepage_sort_by.sort_by_descending()

@then("The products are sorted by descending price")
def step_impl(context):
    context.homepage_sort_by.descending_status()

@when('I click on the "Cele mai noi" option')
def step_impl(context):
    context.homepage_sort_by.sort_by_newest_to_oldest()

@then("The products are sorted by newest to oldest")
def step_impl(context):
    context.homepage_sort_by.newest_to_oldest_status()
