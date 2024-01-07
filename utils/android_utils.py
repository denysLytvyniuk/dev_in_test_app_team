def android_get_desired_capabilities() -> dict:
    """
    Получение настроек для драйвера
    udid определяетсья динамически
    """
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '13',
        'resetKeyboard': True,
        'systemPort': 1000,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


# Данные для тестов
VALID_EMAIL = "qa.ajax.app.automation@gmail.com"
VALID_PASSWORD = "qa_automation_password"
INVALID_EMAIL = "invalid@gmail.com"

# Resource IDs and XPATH
email_input_id = "com.ajaxsystems:id/authLoginEmail"
password_input_id = "com.ajaxsystems:id/authLoginPassword"
login_button_XPATH = "//android.widget.TextView[@text='Вхід']"
sidebar_menu_id = "com.ajaxsystems:id/menuDrawer"
sidebar_settings_button_id = "com.ajaxsystems:id/settings"
return_button_id = "com.ajaxsystems:id/back"
logout_button_XPATH = "//android.widget.TextView[@text='Вихід']"

# hosts
localhost = "http://127.0.0.1:4723"
