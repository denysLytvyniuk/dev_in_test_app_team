import subprocess
import pytest
from utils.driver_initialize import create_driver_with_retries
from utils.logger import get_logger


@pytest.fixture(scope='session')
def run_appium_server():
    """
    Фикстура run_appium_server запускает сервер Appium в фоновом режиме в начале тестовой сессии
    и останавливает его после ее завершения. Это позволяет автоматически управлять жизненным циклом
    сервера Appium, обеспечивая его доступность для всех тестов в сессии.
    """
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )


@pytest.fixture(scope='session')
def driver(run_appium_server):
    """
    Фикстура driver инициализирует и возвращает экземпляр WebDriver для использования в тестах.
    Она использует параметры, определенные в android_get_desired_capabilities, и добавляет udid устройства,
    если таковое доступно. Это обеспечивает подключение к конкретному устройству для выполнения тестов.
    Если устройство не найдено, фикстура прерывает выполнение тестов, сообщая об отсутствии подключенных устройств.

    """
    driver = None
    # Пытаемся создать драйвер
    try:
        driver = create_driver_with_retries()
        yield driver
    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.quit()


@pytest.fixture(scope='session')
def logging():
    """
    Фикстура для логирования во время теста
    """
    logger = get_logger()
    yield logger
