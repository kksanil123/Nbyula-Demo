import pytest

from page_objects.quest_page import QuestPage
from utilities.custom_logger import Loggen


logger = Loggen.get_logger()


@pytest.fixture(scope='module')
def quest_page_object(driver):
    QuestPage(driver).move_to()
    yield QuestPage(driver)
    driver.close()


def test_atleast_one_quest(quest_page_object):
    logger.log(20, 'Questions page Test started')
    no_of_quests = quest_page_object.get_questions()
    assert True if len(no_of_quests) > 0 else pytest.fail('No questions found.', True)
    logger.log(20, 'Questions page Test started')
    pass
