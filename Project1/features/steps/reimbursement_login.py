from behave import *

@given('a user is on the login page')
def test_on_login_page(context):
    context.driver.get('http://localhost:5000/login.html')

@given('a user enters the correct username and password')
def test_user_enters_username_and_password(context):
    context.rl_page.enter_credentials()

@when('the user pushes the submit button')
def test_user_clicks_submit(context):
    context.rl_page.click_to_login()

@then('the user is redirected to the home view page')
def test_user_is_redirected(context):
    assert 'user-home-view.html' in context.driver.current_url

@when('the user hits the enter button')
def test_user_hits_enter(context):
    context.rl_page.press_enter_to_login()


@then('the user is redirected to the home view page anyway')
def test_user_is_redirected_after_using_enter(context):
    assert 'user-home-view.html' in context.driver.current_url