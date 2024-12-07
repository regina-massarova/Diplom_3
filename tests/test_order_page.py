import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data.data import EMAIL, PASSWORD

@allure.feature('Лента заказов')
@allure.story('Тесты функционала ленты заказов')
class TestOrderPage:

    @allure.title('Открытие модального окна с деталями заказа')
    def test_order_modal_opens(self, driver):
        order_page = OrderPage(driver)

        with allure.step('Переходим на страницу ленты заказов'):
            order_page.open_order_page()

        with allure.step('Выбираем последний заказ из списка'):
            order_page.click_last_order()

        with allure.step('Проверяем отображение содержимого модального окна с деталями заказа'):
            content = order_page.get_order_details_content()
            assert content != "", "Модальное окно с деталями заказа не открылось"

    @allure.title('Отображение заказов пользователя в ленте')
    def test_user_orders_displayed_in_feed(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизуемся в аккаунте'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Создаём новый заказ, добавляя ингредиенты'):
            main_page.drag_and_drop_ingredient()
            order_page.click_place_an_order()

        with allure.step('Сохраняем идентификатор созданного заказа'):
            order_id = order_page.get_order_id_from_details()

        with allure.step('Закрываем окно деталей заказа и переходим в ленту заказов'):
            order_page.click_close_order_details()
            order_page.open_order_page()

        with allure.step('Проверяем наличие созданного заказа в ленте заказов'):
            assert order_page.is_order_id_in_feed(order_id), \
                f"Идентификатор заказа {order_id} не найден в ленте заказов"

    @allure.title('Увеличение общего счётчика заказов после нового заказа')
    def test_total_orders_counter_increases_after_new_order(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Выполняем вход в личный кабинет'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем ленту заказов и фиксируем начальный счётчик'):
            order_page.click_feed()
            initial_total_orders = order_page.get_total_orders_counter()

        with allure.step('Создаём новый заказ с добавлением ингредиентов'):
            order_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_page.click_place_an_order()
            order_page.get_order_id_from_details()
            order_page.click_close_order_details()

        with allure.step('Проверяем обновлённое значение общего счётчика заказов'):
            order_page.open_order_page()
            updated_total_orders = order_page.get_total_orders_counter()
            assert updated_total_orders > initial_total_orders, \
                f"Счётчик заказов не увеличился! Было: {initial_total_orders}, стало: {updated_total_orders}"

    @allure.title('Увеличение счётчика заказов за сегодня')
    def test_today_orders_counter_increases_after_new_order(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизуемся и переходим в ленту заказов'):
            account_page.login(EMAIL, PASSWORD)
            order_page.click_feed()

        with allure.step('Фиксируем начальный счётчик заказов за сегодня'):
            initial_today_orders = order_page.get_today_completed_counter()

        with allure.step('Создаем новый заказ'):
            order_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_page.click_place_an_order()
            order_page.get_order_id_from_details()


        with allure.step('Проверяем обновлённое значение счётчика заказов за сегодня'):
            order_page.click_close_order_details()
            order_page.click_feed()

        with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
            updated_today_orders = order_page.get_today_completed_counter()
            assert updated_today_orders > initial_today_orders, \
                f"Счётчик заказов за сегодня не увеличился! Было: {initial_today_orders}, стало: {updated_today_orders}"

    @allure.title('Отображение номера заказа в разделе "В работе"')
    def test_order_number_appears_in_in_progress_after_order_placement(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизуемся в аккаунте'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Создаем новый заказ'):
            order_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_page.click_place_an_order()

        with allure.step('Фиксируем идентификатор нового заказа'):
            order_id = order_page.get_order_id_from_details()

        with allure.step('Закрываем окно с деталями заказа и проверяем раздел "В работе"'):
            order_page.click_close_order_details()
            order_page.click_feed()

        with allure.step('Проверяем, что номер нового заказа отображается в разделе "В работе"'):
            assert order_page.is_order_number_in_progress(order_id), \
                f"Номер заказа {order_id} не найден в разделе 'В работе'"
