from behave import given, when, then
from time import sleep

@then('Verify the language has changed')
def verify_language(context):
    sleep(5)
    context.app.search_results_page.verify_results()

