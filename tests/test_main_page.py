import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data.data import EMAIL, PASSWORD

@allure.feature('Основной функционал')
@allure.story('Тесты функционала главной страницы')
class TestMainPage:

    @allure.title('Переход в конструктор бургеров')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу авторизации'):
            account_page.open_login_page()

        with allure.step('Переходим в секцию "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Проверяем, что отображается раздел  "Собери бургер"'):
            assert main_page.is_burger_constructor_visible(), "Секция 'Собери бургер' не отображается!"

    @allure.title('Переход в ленту заказов')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу авторизации'):
            account_page.open_login_page()

        with allure.step('Переходим в раздел "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Проверяем, что отображается счетчик выполненных заказов'):
            assert main_page.is_order_feed_counter_visible(), "Счетчик выполненных заказов не отображается!"

    @allure.title('Просмотр деталей ингредиента')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу авторизации'):
            account_page.open_login_page()

        with allure.step('Переходим в секцию "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Выбираем ингредиент из списка'):
            main_page.click_ingredient()

        with allure.step('Проверяем, что отображается детали выбранного ингредиента'):
            assert main_page.is_ingredient_details_visible(), "Детали ингредиента не отображаются!"

    @allure.title('Закрытие окна деталей ингредиента')
    def test_close_details(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу авторизации'):
            account_page.open_login_page()

        with allure.step('Переходим в секцию "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Выбираем ингредиент'):
            main_page.click_ingredient()

        with allure.step('Закрываем окно с деталями ингредиента'):
            main_page.close_ingredient_details()

        with allure.step('Проверяем, что окно с деталями ингредиента закрыто'):
            assert not main_page.is_ingredient_details_visible()

    @allure.title('Увеличение счетчика ингредиентов')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу авторизации'):
            account_page.open_login_page()

        with allure.step('Переходим в секцию "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Получаем текущее значение счетчика ингредиентов'):
            initial_counter = main_page.get_ingredient_counter()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingredient()

        with allure.step('Проверяем, что значение счетчика увеличилось'):
            updated_counter = main_page.get_ingredient_counter()

        assert updated_counter == initial_counter + 2, \
            f"Счетчик не увеличился! Ожидалось: {initial_counter + 2}, получено: {updated_counter}"

    @allure.title('Создание заказа для авторизованного пользователя')
    def test_order_creation_for_logged_in_user(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу авторизации'):
            account_page.open_login_page()

        with allure.step('Авторизуемся под тестовым пользователем'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Переходим в конструктор бургеров'):
            main_page.click_constructor()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingredient()

        with allure.step('Подтверждаем создание заказа'):
            main_page.click_place_an_order()

        with allure.step('Проверяем сообщение об успешном создании заказа'):
            success_message = main_page.get_order_success_message()
            assert success_message == "Ваш заказ начали готовить", \
                f"Ожидалось сообщение: 'Ваш заказ начали готовить', но получено: {success_message}"
