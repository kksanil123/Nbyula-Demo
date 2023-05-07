from utilities import read_properties
from selenium.webdriver.common.by import By


class ListingsPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitlywait(5)

    def move_to(self):
        self.driver.get(read_properties.get_listings_page_url())

    def click_ielts_listing_btn(self):
        self.driver.find_element(By.XPATH, '//div[text()="Highest Rated Listings"]/parent::div//div[text()="IELTS Preparation"]')

    def get_ielts_listing_details(self):
        self.driver.find_element(By.XPATH, '//div[text()="Highest Rated Services"]/parent::div//div[@class="slick-track"]/div')



