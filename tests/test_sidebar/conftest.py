import pytest
from framework.main_page import MainPage


@pytest.fixture(scope='session')
def main_window_fixture(driver):
    driver.reset()
    yield MainPage(driver)
