import pytest
from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    """
    Фикстура для создания экземпляра страницы логина предоставляет тестам экземпляр класса LoginPage, который инкапсулирует
    все методы и элементы страницы логина приложения. Вся логика взаимодействия с элементами
    страницы скрыта внутри класса LoginPage, что позволяет тестам быть более чистыми и понятными.
    """
    # я пробовал через close_app и launch_app, то почему-то не launch_app выдавет ошибку
    driver.reset()
    yield LoginPage(driver)
