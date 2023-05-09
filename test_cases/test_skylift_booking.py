import random
import string
import pytest
from utilities.custom_logger import Loggen
from page_objects.book_skylift import SkyLift
from page_objects.signup_page import SignUpPage
from selenium.common.exceptions import NoSuchElementException

logger = Loggen.get_logger()


@pytest.fixture(scope='module')
def signin_page_object(driver):
    SignUpPage(driver).move_to()
    yield SignUpPage(driver)
    driver.close()


@pytest.fixture(scope='module')
def skylift_page_object(driver):
    SkyLift(driver).move_to()
    yield SkyLift(driver)


@pytest.fixture(scope='module')
def login_details():
    global email, password
    with open(r'TestData\StoreLogins.txt', 'r') as file:
        pairs = file.read().split('\n')

    if len(pairs) > 0 and len(pairs[-1])>0 :
        s = pairs[-1].split(':')
        email = s[0].strip('{\'')
        password = s[1].strip('\'} ')
    else:
        print(len(pairs), len(pairs[-1]))
        print(pairs, pairs[-1])
        pytest.skip("No Accounts available to login. Please check Test data folder.")
    logger.log(20, 'Fetched login details')
    return email, password


@pytest.fixture(scope='module')
def mobile_no():
    return int(''.join(random.choices(string.digits, k=10)))


@pytest.fixture(scope='module')
def login(signin_page_object, login_details):
    email, password = login_details
    signin_page_object.set_email_field(email)
    signin_page_object.click_continue_button()
    signin_page_object.set_password(password)
    signin_page_object.click_continue_button()
    yield True


def test_book_skylift(login, skylift_page_object, mobile_no):
    logger.log(20, 'Skylift booking Test started.')
    if login:
        logger.log(20, 'Login successful')
        if skylift_page_object.check_join_converstaion_btn():
            pytest.xfail("User has already joined the event", True)
        else:
            if skylift_page_object.bookinig_status() !='Proceed':
                skylift_page_object.click_book_my_seat_btn()
            else:
                pass
            try:
                skylift_page_object.click_proceed_btn()
                skylift_page_object.click_confirm_btn()
                skylift_page_object.set_mobile_number(mobile_no)
                skylift_page_object.disable_whatsapp_checkbox()
                skylift_page_object.click_continue_btn()
            except NoSuchElementException as e:
                    pytest.fail('Button clicking failed', True)
    else:
        pytest.fail('Login unsuccessful', True)

    skylift_page_object.move_to()
    if skylift_page_object.check_join_converstaion_btn():
        assert True
    else:
        pytest.fail('Join conversation button not available', True)
    logger.log(20, 'Skylift booking Test ended.')
