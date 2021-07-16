from behave import *

@given('the manager is on the view all reimbursement requests')
def test_on_manager_reimbursement_view(context):
    context.driver.get('http://localhost:5000/manager-reimbursement-view.html')

@when('the manager hits the sign out button')
def test_manager_clicks_log_out_button(context):
    context.mav_page.go_to_login()

@then('the manager redirected to the login page')
def test_manager_is_redirected(context):
    assert 'login.html' in context.driver.current_url