from behave import *

@given('the user is on the view all reimbursement requests')
def test_on_user_reimbursement_view(context):
    context.driver.get('http://localhost:5000/user-all-reimbursement-requests.html')

@when('the user hits the sign out button')
def test_user_clicks_log_out_button(context):
    context.uav_page.go_to_login()

@then('the user redirected to the login page')
def test_user_is_redirected(context):
    assert 'login.html' in context.driver.current_url