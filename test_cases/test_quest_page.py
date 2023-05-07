import pytest

from page_objects.quest_page import QuestPage
from utilities.custom_logger import Loggen


@pytest.fixture(scope='module')
def quest_page_object(driver):
    QuestPage(driver).move_to()
    yield QuestPage(driver)
    driver.close()


def test_atleast_one_quest(quest_page_object):
    Loggen.get_logger().log(20, 'Test quest started')
    no_of_quests = quest_page_object.get_questions()
    assert True if len(no_of_quests) > 0 else False
    Loggen.get_logger().log(20, 'Test quest stopped')
    pass
