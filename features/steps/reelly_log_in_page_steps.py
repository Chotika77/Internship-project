from behave import given, when, then
from time import sleep


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.log_in()
