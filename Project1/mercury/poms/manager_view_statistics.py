
class ManagerStatistics:
    home_button = "home-button"

    def __init__(self, driver):
        self.driver = driver

    def go_home(self):
        self.driver.find_element_by_id(self.home_button).click()
