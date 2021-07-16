from selenium import webdriver
from mercury.poms.reimbursement_login import ReimbursementLogin
from mercury.poms.user_reimbursement_view import UserReimbursementView
from mercury.poms.user_view_all_reimbursement_requests import UserAllView
from mercury.poms.manager_login import ManagerLogin
from mercury.poms.manager_view_all import ManagerAllView
from mercury.poms.manager_view_statistics import ManagerStatistics

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='/Users/amrab/Downloads/chromedriver_win32/chromedriver')
    context.rl_page = ReimbursementLogin(context.driver)
    context.urv_page = UserReimbursementView(context.driver)
    context.uav_page = UserAllView(context.driver)
    context.ml_page = ManagerLogin(context.driver)
    context.mav_page = ManagerAllView(context.driver)
    context.ms_page = ManagerStatistics(context.driver)

def after_all(context):
    context.driver.quit()
