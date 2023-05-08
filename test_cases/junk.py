# import logging
#
# from utilities.custom_logger import Loggen
#
#
# def test_sample():
#     Loggen.get_logger().info('Test started')
#     Loggen.get_logger().info('Test stopped')
#     assert True

def get_login_details():
    with open(r'..\TestData\StoreLogins.txt', 'r') as file:
        pairs = file.read().split('\n')

    s = pairs[-1].split(':')
    email = s[0].strip('{\'')
    password = s[1].strip('\'} ')
    return email, password


print(type(get_login_details()))
