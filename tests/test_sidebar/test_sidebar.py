def test_open_sidebar(logging, main_window_fixture):
    """
    Тест проверки открытия меню Sidebar
    Проверка идет на наличие кнопки Найстройки по resourse_id
    """
    logging.debug("Starting test: Открывается ли меню Sidebar....")

    main_window_fixture.open_sidebar()
    logging.debug("Открытие меню")

    is_opened = main_window_fixture.is_element_displayed(main_window_fixture.SIDEBAR_MENU_SETTINGS)
    logging.debug("Проверка открытия")

    if not is_opened:
        raise AssertionError("Меню не было открыто.")

    logging.debug(f"Тест завершен УСПЕШНО - проверка открытия меню Sidebar")


def test_open_sidebar_settings(logging, main_window_fixture):
    """
    Тест проверки открытия настроек в меню Sidebar
    Проверка идет на наличие кнопки выхода в найстройках по XPATH
    """
    logging.debug("Starting test: Открываются ли меню настройки....")
    main_window_fixture.open_sidebar()
    logging.debug("Открытие меню Sidebar")

    main_window_fixture.click_element(main_window_fixture.SIDEBAR_MENU_SETTINGS)
    logging.debug("Нажатие кнопки настроек")

    is_opened = main_window_fixture.is_element_displayed(main_window_fixture.LOGOUT_BUTTON)
    logging.debug("Проверка открытия")

    if not is_opened:
        raise AssertionError("Настройки не были открыты.")

    logging.debug(f"Тест завершен УСПЕШНО - проверка открытия настроек в меню Sidebar")
    main_window_fixture.click_element(main_window_fixture.RETURN_BUTTON)


def test_logout(logging, main_window_fixture):
    """
    Тест функционала выхода из системы
    До нажатия кнопки мы пытаемся нажать все нужные кнопки по очереди, причем если мы уже на каком то этапе, то ничего
    не ломается
    Проверка идет на наличие кнопки входа по XPATH
    """
    logging.debug("Starting test: Попытка выйти из системы....")
    main_window_fixture.open_sidebar()
    logging.debug("Открытие меню")

    main_window_fixture.open_settings()
    logging.debug("Открытие настроек")

    main_window_fixture.logout()
    logging.debug("Нажатие кнопки выхода")

    is_opened = main_window_fixture.is_element_displayed(main_window_fixture.LOGIN_BUTTON)
    logging.debug("Проверка выхода")

    if not is_opened:
        raise AssertionError("Результат входа не соответствует ожидаемому.")

    logging.debug(f"Тест завершен УСПЕШНО - проверка выхода из системы")
