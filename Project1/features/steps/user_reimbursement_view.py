from behave import *

@given('the user on the reimbursement view page')
def test_on_user_reimbursement_view(context):
    context.driver.get('http://localhost:5000/user-reimbursement-view.html')

@given('the user enters the reimbursement reason and the user enters the reimbursement amount')
def test_user_enters_reimbursement_reason_and_amount(context):
    context.urv_page.add_request()

@when('the user hits the home page button')
def test_user_clicks_home_button(context):
    context.urv_page.go_home()

@then('the user redirected to the home page')
def test_user_is_redirected(context):
    assert 'user-home-view.html' in context.driver.current_url

