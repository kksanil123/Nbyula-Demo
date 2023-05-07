from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utilities import read_properties


class QuestPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def move_to(self):
        self.driver.get(read_properties.get_home_page_url())
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element(By.XPATH, '//div[text()="Explore"]'))
        act.click(self.driver.find_element(By.XPATH, '//li[text()="Quest"]/parent::a'))
        act.perform()

    def get_questions(self):
        return self.driver.find_elements(By.XPATH, '//section[@class="relative"]//article')
