from utilities import read_properties
from selenium.webdriver.common.by import By


class SkyLift():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitlywait(5)

    def move_to(self):
        self.driver.get(read_properties.get_skylift_page_url())

    def click_book_my_seat_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Book My Seat"]')

    def click_proceed_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Proceed"]')

    def click_confirm_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Confirm FREE Booking"]')

