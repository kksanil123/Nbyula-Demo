from utilities import read_properties
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(read_properties.get_home_page_url())
        self.driver.implicitly_wait(5)

    def get_logo(self):
        return self.driver.find_element(By.XPATH, '//*[@id="navbar-home"]')

    def get_menu_button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="navbar-profile-dropdown"]')
            return True
        except NoSuchElementException as e:
            return False
