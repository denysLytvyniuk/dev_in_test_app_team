from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Page:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """Метод для ожидания элемента."""
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException

    def wait_for_element_to_be_clicable(self, locator, timeout=10):
        """Метод для ожидания элемента."""
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException

    def find_element(self, locator):
        """Метод для поиска элемента с ожиданием."""
        return self.wait_for_element(locator)

    def click_element(self, locator):
        """Метод для клика по элементу с ожиданием."""
        if self.is_element_displayed(locator):
            element = self.wait_for_element_to_be_clicable(locator)
            element.click()
            return True
        return False

    def is_element_displayed(self, element: tuple[str, str]) -> bool:
        """
        Метод для проверки есть ли елемент на странице
        """
        try:
            self.find_element(element)
            return True
        except:
            return False
