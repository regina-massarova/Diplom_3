from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locator(self, locator, num):
        method, locator_str = locator
        locator_str = locator_str.format(num)
        return method, locator_str


    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click_with_js(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_element_visible(self, locator):

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )

    def drag_and_drop(self, source_locator, target_locator):
        """
        Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
        :param source_locator: Локатор элемента, который нужно перетащить.
        :param target_locator: Локатор элемента, куда нужно перетащить.
        """
        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    def is_element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_until_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)
