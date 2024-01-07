import pytest
from framework.main_page import MainPage


@pytest.fixture(scope='session')
def main_window_fixture(driver):
    """
    Фикстура которая один раз создает обьект MainPage, который при инициализации заходит в главное меню
    """
    driver.reset()
    yield MainPage(driver)
