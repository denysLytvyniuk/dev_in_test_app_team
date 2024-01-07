import time

from utils.android_utils import login_button_XPATH, email_input_id, password_input_id

from appium.webdriver.common.mobileby import MobileBy


from framework.page import Page


class LoginPage(Page):
    """
    Класс LoginPage предоставляет функционал для взаимодействия со страницей входа в приложение.
    В нем определены методы для ожидания, поиска и взаимодействия с элементами страницы логина,
    такими как поля ввода для имени пользователя и пароля, а также кнопка входа.

    Методы:
    - wait_for_element: Ожидает появления элемента на странице до истечения таймаута.
    - wait_for_element_to_be_clicable: Ожидает, пока элемент не станет кликабельным.
    - find_element: Ищет элемент с ожиданием его появления.
    - click_element: Кликает по элементу после его появления и обеспечения кликабельности.
    - enter_username: Вводит имя пользователя в соответствующее поле.
    - enter_password: Вводит пароль в соответствующее поле.
    - press_login_button: Нажимает кнопку входа.
    - find_login_button: Ищет кнопку входа.
    - close: Закрывает драйвер и завершает сессию.

    """
    EMAIL_INPUT = (MobileBy.ID, email_input_id)
    PASSWORD_INPUT = (MobileBy.ID, password_input_id)
    LOGIN_BUTTON = (MobileBy.XPATH, login_button_XPATH)

    def enter_username(self, username):
        """Метод для ввода имени пользователя."""
        username_input = self.find_element(self.EMAIL_INPUT)
        username_input.send_keys(username)

    def enter_password(self, password):
        """Метод для ввода пароля."""
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def press_login_button(self):
        """Метод для нажатия кнопки логина."""
        self.click_element(self.LOGIN_BUTTON)

    def find_login_button(self):
        """Метод для поиска кнопки логина."""
        return self.find_element(self.LOGIN_BUTTON)

    def login(self, email, password):

        self.press_login_button()

        self.enter_username(email)

        self.enter_password(password)

        self.press_login_button()

    def check_if_logged_in(self):
        return self.is_element_displayed(self.LOGIN_BUTTON)

    def close(self):
        """Метод для завершения драйвера"""
        self.driver.quit()


