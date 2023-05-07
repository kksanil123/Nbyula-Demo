from utilities import read_properties
from selenium.webdriver.common.by import By


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)


    def set_email_field(self, email):
        self.driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(email)

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, '//button[@id="login-custom"]').click()

    def set_first_name(self, firstname):
        self.driver.find_element(By.XPATH, '//input[@placeholder="First name"]').send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Last name"]').send_keys(lastname)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, '//button[@variant="primary"]').click()

    def set_otp(self, otp):
        self.driver.find_element(By.XPATH, '//input[@type="number"]').send_keys(otp)

    def click_confirm_button(self):
        self.driver.find_element(By.XPATH,  '//button[@id="verification-confirm-otp"]').click()

