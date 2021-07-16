from behave import *

@given('a manager is on the login page')
def test_on_login_page(context):
    context.driver.get('http://localhost:5000/login.html')

@given('a manager enters the correct username and password')
def test_manager_enters_username_and_password(context):
    context.ml_page.enter_credentials()

@when('the manager pushes the submit button')
def test_manager_clicks_submit(context):
    context.ml_page.click_to_login()

@then('the manager is redirected to the home view page')
def test_manager_is_redirected(context):
    assert 'manager-home-view.html' in context.driver.current_url

@when('the manager hits the enter button')
def test_manager_hits_enter(context):
    context.ml_page.press_enter_to_login()


@then('the manager is redirected to the home view page anyway')
def test_manager_is_redirected_after_using_enter(context):
    assert 'manager-home-view.html' in context.driver.current_url