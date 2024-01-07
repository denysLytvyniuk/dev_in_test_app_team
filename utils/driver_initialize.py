import subprocess
import socket
import time

from appium import webdriver

from utils.android_utils import android_get_desired_capabilities, localhost


def create_driver_with_retries(max_retries=5, wait_interval=2):
    """
    Метод создания appium драйвера
    1. Получение активного подключеного устройства
    2. Проверка достпных портов
    3. Подключение
    """
    # Получения первого подключеного устройства
    capabilities = android_get_desired_capabilities()
    udid = get_udid()
    if udid:
        capabilities['udid'] = get_udid()
    else:
        raise Exception("Нету подключенных устройств")
    # Проверка доступности порта
    for attempt in range(max_retries):
        port = capabilities['systemPort']
        if not is_port_available(port):
            print(f"Порт {port} занят, попытка {attempt + 1} из {max_retries}...")
            capabilities['systemPort'] = port + 1
            time.sleep(wait_interval)
        else:
            try:
                # Создание драйвера
                driver = webdriver.Remote(localhost, capabilities)
                return driver
            except Exception as e:
                raise Exception(f"Ошибка при попытке создания сессии: {e}")
    raise Exception("Не удалось создать драйвер после нескольких попыток")


def get_udid():
    """
    Метод получение первого активного подключеного устройства с помощью subprocess
    """
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
    lines = result.stdout.decode().split('\n')
    for line in lines[1:]:
        if "device" in line:
            # Получение первого подключенного устройства
            return line.split('\t')[0]
    return None


def is_port_available(port):
    """
    Проверка доступен ли порт
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result != 0  # Если 0, то порт уже занят
