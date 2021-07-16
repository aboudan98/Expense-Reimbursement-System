from behave import *

@given('the manager is on the statistics page')
def test_on_manager_reimbursement_view(context):
    context.driver.get('http://localhost:5000/statistics.html')

@when('the manager hits the home button')
def test_manager_clicks_log_out_button(context):
    context.ms_page.go_home()

@then('the manager redirected to the home page')
def test_manager_is_redirected(context):
    assert 'manager-home-view.html' in context.driver.current_url