import logging

from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
from urllib3.connectionpool import log as urllibLogger

# Исключил с логирования обычные логи этих библиотек
seleniumLogger.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)


def get_logger():
    return logging
