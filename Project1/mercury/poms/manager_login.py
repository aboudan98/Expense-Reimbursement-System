from selenium.webdriver.common.keys import Keys

class ManagerLogin:
    # Let's define the elements that should exist in this repository. Note that I'm
    # only using the locators here.
    username_box_id = 'username'
    password_box_id = 'password'
    login_button_id = 'submit-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        self.driver.find_element_by_id(self.username_box_id).send_keys('manager1')
        self.driver.find_element_by_id(self.password_box_id).send_keys('password')

    def click_to_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def press_enter_to_login(self):
        self.driver.find_element_by_id(self.password_box_id).send_keys(Keys.ENTER)