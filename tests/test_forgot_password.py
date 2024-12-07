import allure
from pages.forgot_password_page import ForgotPasswordPage
from data.data import EMAIL


@allure.feature('Восстановление пароля')
@allure.story('Тесты функционала восстановления пароля')
class TestForgotPasswordPage:

    @allure.title('Переход на страницу восстановления пароля')
    def test_navigate_to_forgot_password_page(self, driver):
        forgot_password_page = ForgotPasswordPage (driver)

        with allure.step('Переходим на страницу авторизации'):
            forgot_password_page.open_login_page()

        with allure.step('Нажимаем ссылку "Забыли пароль?" для перехода'):
            forgot_password_page.navigate_to_forgot_password_page()

        with allure.step('Проверяем, что кнопка "Восстановить" отображается на странице'):
            assert forgot_password_page.is_recover_button_visible(), \
                "Не удалось попасть на страницу восстановления пароля"

    @allure.title('Процесса восстановления пароля через e-mail')
    def test_password_recovery(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)

        with allure.step('Открываем страницу авторизации'):
            forgot_password_page.open_login_page()

        with allure.step('Кликаем по ссылке для восстановления пароля'):
            forgot_password_page.navigate_to_forgot_password_page()

        with allure.step('Заполняем поле email для восстановления пароля'):
            forgot_password_page.enter_email(EMAIL)

        with allure.step('Нажимаем кнопку "Восстановить"'):
            forgot_password_page.click_recover_button()

        with allure.step('Проверяем, что отображается поле для ввода нового пароля'):
            assert forgot_password_page.is_new_password_input_visible(), \
                "Не удалось перейти к вводу нового пароля"

    @allure.title('Переключение видимости пароля при восстановлении')
    def test_toggle_password_visibility(self, driver):
        forgot_password_page = ForgotPasswordPage (driver)

        with allure.step('Открываем страницу авторизации'):
            forgot_password_page.open_login_page()

        with allure.step('Переходим на страницу восстановления пароля через ссылку'):
            forgot_password_page.navigate_to_forgot_password_page()

        with allure.step('Вводим email для начала процесса восстановления'):
            forgot_password_page.enter_email(EMAIL)

        with allure.step('Нажимаем кнопку "Восстановить" для подтверждения'):
            forgot_password_page.click_recover_button()

        with allure.step('Изменяем видимость вводимого пароля'):
            forgot_password_page.toggle_password_visibility()

        with allure.step('Проверяем, что пароль отображается корректно'):
            updated_type = forgot_password_page.get_password_input_type()
            assert updated_type == "text", "Поле пароля должно быть видимым"