from configparser import RawConfigParser

config = RawConfigParser()
config.read(r'Configuration/config.ini')


def get_app_url():
    app_url: str = config.get('website-info', 'app_url')
    return app_url


def get_home_page_url():
    home_page_url: str = config.get('website-info', 'home_page_url')
    return home_page_url


def get_signin_page_url():
    signin_page_url: str = config.get('website-info', 'signin_page_url')
    return signin_page_url


def get_skylift_page_url():
    skylift_page_url: str = config.get('website-info', 'skylift_page_url')
    return skylift_page_url


def get_listings_page_url():
    listings_page_url: str = config.get('website-info', 'listings_page_url')
    return listings_page_url
