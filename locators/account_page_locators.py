from selenium.webdriver.common.by import By

class AccountPageLocators:

    # Кнопка "Личный кабинет"
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # Поле ввода почты
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')

    # Локатор успешного входа в личный кабинет (кнопка "Выход")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

    # Кнопка "История заказов"
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

    # Выполненные заказы в "Историях заказов"
    ORDER_COMPLETED = (By.XPATH, "//p[@class='OrderHistory_visible__19YMB text text_type_main-small mb-7']")

    # Кнопка "Вход, после выхода из кабинета"
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")

    # Локатор успешного входа
    # Локатор успешного входа
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Оформить заказ')]")