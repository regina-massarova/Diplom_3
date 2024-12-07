import allure
from data.data import EMAIL, PASSWORD
from pages.account_page import AccountPage


@allure.feature('Личный кабинет')
@allure.story('Тесты функционала личного кабинета')
class TestAccountPage:

    @allure.title('Вход в аккаунт и проверка отображения личного кабинета')
    def test_click_account_button(self, driver):
        account_page = AccountPage(driver)

        with allure.step('Авторизуемся с валидными данными пользователя'):
            account_page.login(EMAIL, PASSWORD)
        with allure.step('Открываем страницу личного кабинета'):
            account_page.click_account_button()


        with allure.step('Проверяем, что элемент "Выход" присутствует на странице'):
            assert account_page.is_logout_button_visible(), \
                "Не удалось войти в личный кабинет"

    @allure.title('Просмотр истории заказов через личный кабинет')
    def test_click_order_history(self, driver):
        account_page = AccountPage(driver)

        with allure.step('Авторизуемся с валидными данными пользователя'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Переходим в личный кабинет'):
            account_page.click_account_button()
        with allure.step('Открываем раздел "История заказов"'):
            account_page.click_order_history_button()


        with allure.step('Проверяем наличие завершенного заказа в истории'):
            assert account_page.is_order_completed(), \
                "Не удалось перейти в историю заказов или завершенный заказ отсутствует"

    @allure.title('Выход из аккаунта через личный кабинет')
    def test_logout(self, driver):
        account_page = AccountPage(driver)

        with allure.step('Авторизуемся с валидными данными пользователя'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем страницу личного кабинета'):
            account_page.click_account_button()

        with allure.step('Выходим из аккаунта через кнопку "Выход"'):
            account_page.click_logout_button()

        with allure.step('Проверяем, что после выхода отображается кнопка "Вход"'):
            assert account_page.is_login_button_visible_after_logout(), \
                "Не удалось выйти из аккаунта"

