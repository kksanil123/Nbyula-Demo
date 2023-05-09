import time

from utilities import read_properties
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con


class SkyLift():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)

    def move_to(self):
        time.sleep(5)
        self.driver.get(read_properties.get_skylift_page_url())

    def click_book_my_seat_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Book My Seat"]').click()

    def click_proceed_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Proceed"]').click()

    def click_confirm_btn(self):
        wait = WebDriverWait(self.driver, timeout=5)
        wait.until(exp_con.visibility_of_element_located((By.XPATH, '//span[text()="India"]')))
        wait.until(exp_con.visibility_of_element_located((By.XPATH, '//span[text()="India"]')))
        self.driver.find_element(By.XPATH, '//span[text()="Confirm FREE Booking"]').click()

    def set_mobile_number(self, number):
        self.driver.find_element(By.XPATH, '//div[text()="Phone"]/following-sibling::input').send_keys(number)

    def disable_whatsapp_checkbox(self):
        self.driver.find_element(By.XPATH, '//input[@type="checkbox"]/following-sibling::div[2]').click()

    def check_join_converstaion_btn(self):
        try:
            wait = WebDriverWait(self.driver, timeout=3)
            wait.until(exp_con.visibility_of_element_located((By.XPATH, '//span[text()="Join Conversation"]')))
            self.driver.find_element(By.XPATH, '//span[text()="Join Conversation"]')
        except Exception:
            return False

        return True

    def bookinig_status(self):
        return self.driver.find_element(By.XPATH, '//button[@id="skylift-proceed-to-purchase"]/span').text

    def click_continue_btn(self):
        self.driver.find_element(By.XPATH, '//span[text()="Continue"]').click()
