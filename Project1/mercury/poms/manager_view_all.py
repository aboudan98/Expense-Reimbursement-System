
class ManagerAllView:
    sign_out_button = "sign-out-button"

    def __init__(self, driver):
        self.driver = driver

    def go_to_login(self):
        self.driver.find_element_by_id(self.sign_out_button).click()
