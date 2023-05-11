import string
import pytest
import random
from selenium.webdriver.common.by import By
from page_objects.home_page import HomePage
from page_objects.signup_page import SignUpPage
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as exp_con
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from utilities.custom_logger import Loggen

logger = Loggen.get_logger()
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
    logger.log(20, 'Fetch OTP fixture started')
    wait = WebDriverWait(driver, timeout=8, ignored_exceptions=[TimeoutException])
    driver.switch_to.new_window('window')
    driver.get("https://yopmail.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your inbox here"]').send_keys(email)
    driver.find_element(By.XPATH, '//button[@class="md"]').click()
    try:
        wait.until(exp_con.element_to_be_clickable((By.XPATH, '//button[@id="refresh"]')))
        driver.find_element(By.XPATH, '//button[@id="refresh"]').click()
    except ElementClickInterceptedException:
        pytest.skip("Skipping this test, since human verfification is needed.")
    wait.until(exp_con.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@name="ifinbox"]')))
    if exp_con.visibility_of_element_located((By.XPATH, '//span[text()="Nbyula"]')):
        driver.find_element(By.XPATH, '//span[text()="Nbyula"]').click()
    else:
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, '//button[@id="refresh"]').click()
    driver.switch_to.default_content()
    driver.switch_to.frame('ifmail')
    email_subject = driver.find_element(By.XPATH, '//div[@class="ellipsis nw b f18"]').text
    driver.switch_to.default_content()
    driver.switch_to.window(driver.window_handles[0])
    logger.log(20, 'Fetch OTP fixture ended')
    yield email_subject[0:6]


@pytest.fixture()
def email_signup(signup_page_object, email, request, password):
    logger.log(20, 'Email signup started.')
    signup_page_object.set_email_field(email)
    signup_page_object.click_continue_button()
    signup_page_object.set_first_name('Kishore')
    signup_page_object.set_last_name('Testing')
    signup_page_object.set_password(password)
    signup_page_object.click_signup_button()
    otp = request.getfixturevalue('fetch_otp')
    signup_page_object.set_otp(otp)
    signup_page_object.click_confirm_button()
    logger.log(20, 'Email signup finished.')
    yield None


def test_email_signup_success(email_signup, email, password, home_page_object):
    logger.log(20, 'Email signup success Test started.')
    if home_page_object.get_menu_button():
        with open(r'TestData/StoreLogins.txt', 'a') as file:
            file.writelines(['\n',str({email: password}),])
        logger.log(20, 'Storing email and password.')
        assert True
    else:
        assert pytest.fail('Login failed', True)

    logger.log(20, 'Email signup success Test ended.')
