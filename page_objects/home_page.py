from utilities import read_properties
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def move_to(self):
        self.driver.get(read_properties.get_home_page_url())

    def click_logo_btn(self):
        return self.driver.find_element(By.XPATH, '//a[@id="navbar-home"]')

    def click_study_abroad_btn(self):
        return self.driver.find_element(By.XPATH, '//a[@id="navbar-home"]/following::div//a[text()="Study Abroad"]')

    def get_page_title(self):
        return self.driver.current_url

    def get_menu_button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="navbar-profile-dropdown"]')
            return True
        except NoSuchElementException as e:
            return False
