from selenium.webdriver.common.keys import Keys

class UserReimbursementView:
    reason_id = 'reason'
    amount_id = 'reimbursement-amount'
    home_id = 'home-button'

    def __init__(self, driver):
        self.driver = driver


    def add_request(self):
        self.driver.find_element_by_id(self.reason_id).send_keys('This is a test reason')
        self.driver.find_element_by_id(self.amount_id).send_keys('100')

    def go_home(self):
        self.driver.find_element_by_id(self.home_id).click()
