from utilities import read_properties
from selenium.webdriver.common.by import By


class ListingsPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def move_to(self):
        self.driver.get(read_properties.get_listings_page_url())

    def click_ielts_listing_btn(self):
        self.driver.find_element(By.XPATH,
                                 '//div[text()="Highest Rated Listings"]/parent::div//div[text()="IELTS Preparation"]')

    def get_ielts_listing_details(self):
        return self.driver.find_elements(By.XPATH,
                                         '//div[text()="Highest Rated Listings"]/parent::div//div[@class="slick-track"]/div')

    def get_popular_services(self):
        return self.driver.find_elements(By.XPATH,
                                         '//div[text()="Popular services"]/parent::div//div[@class="slick-track"]/div')

    def print_popular_services(self):
        common_xpath = '//div[text()="Popular services"]/parent::div//div[@class="slick-track"]/div'
        services = self.get_popular_services()
        if len(services) > 0:
            for i in range(len(services)):
                service_name = self.driver.find_element(By.XPATH, common_xpath + f'{[i+1]}' + '//span' + '[2]').text
                service_link = self.driver.find_element(By.XPATH, common_xpath + f'{[i+1]}' + '//img').get_property('src')
                print(service_name, service_link, )
        else:
            print('No services found.')

    def window_scroll(self):
        self.driver.execute_script('window.scrollBy(0,700)')
