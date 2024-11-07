from behave import given, when, then
from time import sleep


@given('open the main page')
def open_main(context):
    context.app.main_page.open_main()

@when('click on the menu')
def click_menu(context):
    context.app.main_page.click_main_menu()


@when('Change the language of the page to Russian')
def change_language(context):
    context.app.main_page.change_language()


