import string
import time
import pytest
import random
from selenium.webdriver.common.by import By
from page_objects.home_page import HomePage
from page_objects.signup_page import SignUpPage
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as exp_con
from selenium.common.exceptions import TimeoutException
from utilities.custom_logger import Loggen

Registered_emails = []


@pytest.fixture(scope='module')
def home_page_object(driver):
    yield HomePage(driver)
    driver.quit()


@pytest.fixture(scope='module')
def signup_page_object(driver):
    SignUpPage(driver).move_to()
    yield SignUpPage(driver)


@pytest.fixture(scope='module')
def email():
    email_gen = 'Test' + str(random.randint(1, 1000)) + '@yopmail.com'
    if email_gen in Registered_emails:
        email = 'Testa' + str(random.randint(1, 1000)) + '@yopmail.com'
    else:
        email = 'Test' + str(random.randint(1, 1000)) + '@yopmail.com'

    Registered_emails.append(email)
    return email


@pytest.fixture(scope='module')
def password():
    return 'Ki'.join(random.choices(string.digits, k=4))


@pytest.fixture(scope='module')
def fetch_otp(driver, email):
    driver.switch_to.new_window('window')
    driver.get("https://yopmail.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your inbox here"]').send_keys(email)
    driver.find_element(By.XPATH, '//button[@class="md"]').click()
    driver.find_element(By.XPATH, '//button[@id="refresh"]').click()
    driver.switch_to.frame('ifinbox')
    wait= WebDriverWait(driver, timeout=5, ignored_exceptions=[TimeoutException])
    wait.until(exp_con.visibility_of_element_located((By.XPATH, '//span[text()="Nbyula"]')))
    driver.switch_to.default_content()
    driver.switch_to.frame('ifmail')
    email_subject = driver.find_element(By.XPATH, '//div[@class="ellipsis nw b f18"]').text
    driver.switch_to.default_content()
    driver.switch_to.window(driver.window_handles[0])
    yield email_subject[0:6]


@pytest.fixture()
def email_signup(signup_page_object, email, request, password):
    Loggen.get_logger().log(10, 'Test signup started', 'Sample printing')
    signup_page_object.set_email_field(email)
    signup_page_object.click_continue_button()
    signup_page_object.set_first_name('Kishore')
    signup_page_object.set_last_name('Testing')
    signup_page_object.set_password(password)
    signup_page_object.click_signup_button()

    otp = request.getfixturevalue('fetch_otp')
    signup_page_object.set_otp(otp)
    signup_page_object.click_confirm_button()
    yield None


def test_email_signup_success(email_signup, email, password, home_page_object):
    if home_page_object.get_menu_button():
        with open(r'TestData/StoreLogins.txt', 'a') as file:
            file.writelines(['\n',str({email: password}),])
        assert True
    else:
        assert pytest.fail('Login failed', True)
