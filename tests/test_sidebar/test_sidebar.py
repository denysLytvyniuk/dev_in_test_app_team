

def test_open_sidebar(logging, main_window_fixture):
    logging.debug("Starting test: Открывается ли меню Sidebar....")

    is_opened = main_window_fixture.open_sidebar()
    logging.debug("Проверка открытия")

    if not is_opened:
        raise AssertionError("Меню не было открыто.")

    logging.debug(f"Тест завершен УСПЕШНО - проверка открытия меню Sidebar")


def test_open_sidebar_settings(logging, main_window_fixture):
    logging.debug("Starting test: Открываются ли меню настройки....")
    main_window_fixture.open_sidebar()

    if not main_window_fixture.is_element_displayed(main_window_fixture.SIDEBAR_MENU_SETTINGS):

        logging.debug("Проверка открытия меню")
        assert False

    main_window_fixture.click_element(main_window_fixture.SIDEBAR_MENU_SETTINGS)
    logging.debug("Нажатие кнопки настроек")

    is_opened = main_window_fixture.is_element_displayed(main_window_fixture.LOGOUT_BUTTON)
    logging.debug("Проверка открытия")

    if not is_opened:
        raise AssertionError("Настройки не были открыты.")

    logging.debug(f"Тест завершен УСПЕШНО - проверка открытия меню Sidebar")
    main_window_fixture.click_element(main_window_fixture.RETURN_BUTTON)


def test_logout(logging, main_window_fixture):
    logging.debug("Starting test: Попытка выйти из системы....")
    if not main_window_fixture.open_sidebar():
        logging.debug("Открытие меню")
        assert False, "Меню не открылось"

    main_window_fixture.open_settings()
    logging.debug("Открытие настроек")

    if not main_window_fixture.is_element_displayed(main_window_fixture.LOGOUT_BUTTON):
        logging.debug("Проверка открытия")
        assert False, "Настройки не открылись"

    main_window_fixture.logout()
    is_opened = main_window_fixture.is_element_displayed(main_window_fixture.LOGIN_BUTTON)

    if not is_opened:
        raise AssertionError("Результат входа не соответствует ожидаемому.")

    logging.debug(f"Тест завершен УСПЕШНО - проверка открытия меню Sidebar")


