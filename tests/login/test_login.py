import time

import pytest

from utils.android_utils import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL


@pytest.mark.parametrize("email,password,expected", [
    (VALID_EMAIL, VALID_PASSWORD, True),  # Позитивный кейс
    (INVALID_EMAIL, VALID_PASSWORD, False)  # Негативный кейс
])
def test_login(logging, user_login_fixture, email, password, expected):
    """
    Тест проверки входа в приложения
    Через параметризацию проверяються позитивный и негативвный кейсы
    Иногда при введеных данных и нажатии кнопки входа в приложении появляется ошибка синхронизации с сервером.
    Я не сделал обработку этого и повторную попытку нажатия, не уверен что это нужно было. Но если нужно, то предпологаю
    нужно определять текст всплывающего окна с текстом о неверном пароле или логине, а не как я проверяю наличие кнопки
    входа.
    """

    logging.debug(f"Starting test: вход пользователя с email {email}")

    user_login_fixture.press_login_button()
    logging.debug("Нажата кнопка входа")

    user_login_fixture.enter_username(email)
    logging.debug(f"Введен email: {email}")

    user_login_fixture.enter_password(password)
    logging.debug(f"Введен пароль: [скрыт]")

    time.sleep(2)

    user_login_fixture.press_login_button()
    logging.debug("Нажатие на кнопку входа")

    time.sleep(3)

    is_logged_in = user_login_fixture.check_if_logged_in()
    logging.debug("Проверка осталась ли кнопка входа...")
    # Так как иногда вылезает ошибка связанная со синхронизацией, я добавил дополнительныq клик по кнопке
    if not is_logged_in:

        user_login_fixture.press_login_button()
        logging.debug("Повторное нажатие на кнопку входа")
        time.sleep(3)
        is_logged_in = user_login_fixture.check_if_logged_in()
        logging.debug("Повторная проверка осталась ли кнопка входа...")

    # Если ожидаемый результат не совпадает с фактическим, вызываем исключение
    if expected != is_logged_in:
        raise AssertionError("Результат входа не соответствует ожидаемому.")

    logging.debug(f"Тест завершен УСПЕШНО - кейс: {'Удачный' if is_logged_in else 'Неудачный'} вход")
