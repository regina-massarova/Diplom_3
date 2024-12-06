from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from config import BASE_URL


class OrderPage(BasePage):
    def click_last_order(self):
        self.click_to_element(OrderPageLocators.LAST_ORDER)

    def get_order_details_content(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_DETAILS_CONTENT)

    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderPageLocators.TOTAL_ORDERS_COUNTER))

    def get_today_completed_counter(self):

        element = self.find_element_with_wait(OrderPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())


    def open_order_page(self):
        self.navigate_to((f"{BASE_URL}/feed"))
        self.wait_for_element_visible(OrderPageLocators.FEED_TITLE)

    def click_constructor(self):
        self.click_to_element(OrderPageLocators.CONSTRUCTOR_BUTTON)

    def click_feed(self):
        self.wait_for_element_visible(OrderPageLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_when_clickable(OrderPageLocators.ORDER_FEED_BUTTON)

    def click_place_an_order(self):
        self.click_to_element(OrderPageLocators.PLACE_AN_ORDER)


    def click_account_button(self):
        self.click_when_clickable(OrderPageLocators.ACCOUNT_BUTTON)

    def click_order_history_button(self):
        self.click_to_element(OrderPageLocators.ORDER_HISTORY_BUTTON)

    def click_close_order_details(self):
        self.click_when_clickable(OrderPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderPageLocators.ORDER_ID)

    def is_order_id_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Добавляем нули до длины 7
        order_locator = OrderPageLocators.ORDER_ID_IN_FEED
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    def is_order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Форматирование с ведущими нулями
        self.find_and_format_locator(OrderPageLocators.ORDER_IN_PROGRESS_LOCATOR, formatted_id)
        return True