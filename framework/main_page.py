import time

from appium.webdriver.common.mobileby import MobileBy

from framework import LoginPage
from utils.android_utils import VALID_EMAIL, VALID_PASSWORD, sidebar_menu_id, sidebar_settings_button_id, \
    logout_button_XPATH, return_button_id


class MainPage(LoginPage):
    SIDEBAR_MENU = (MobileBy.ID, sidebar_menu_id)
    SIDEBAR_MENU_SETTINGS = (MobileBy.ID, sidebar_settings_button_id)
    LOGOUT_BUTTON = (MobileBy.XPATH, logout_button_XPATH)
    RETURN_BUTTON = (MobileBy.ID, return_button_id)

    def __init__(self, driver):
        """
        Метод инициализации который запускает приложения и логиниться в систему
        """
        super().__init__(driver)
        super().login(VALID_EMAIL, VALID_PASSWORD)

        for _ in range(3):
            time.sleep(3)
            logged_in = super().check_if_logged_in()
            if logged_in:
                break
            super().press_login_button()

    def open_sidebar(self) -> bool:
        """
        Метод нажатия на меню Sidebar
        rtype: bool
        """
        if self.is_element_displayed(self.SIDEBAR_MENU):
            self.click_element(self.SIDEBAR_MENU)
            return True
        else:
            return False

    def open_settings(self) -> bool:
        """
        Метод открытия настроек в меню
        rtype: bool
        """
        if self.is_element_displayed(self.SIDEBAR_MENU_SETTINGS):
            self.click_element(self.SIDEBAR_MENU_SETTINGS)
            return True
        else:
            return False

    def logout(self) -> bool:
        """
        Метод выхода с системы
        rtype: bool
        """
        if self.is_element_displayed(self.LOGOUT_BUTTON):
            self.click_element(self.LOGOUT_BUTTON)
            return True
        else:
            return False
