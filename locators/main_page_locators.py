from selenium.webdriver.common.by import By

class MainPageLocators:

        # Кнопка "Конструктор"
        CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

        # Секция "Собери бургер" после нажатия на "Конструктор"
        BURGER_CONSTRUCTOR_SECTION = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")

        # Кнопка "Лента заказов"
        ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

        # Заголовок "Готовы"
        COMPLETED_ORDERS = (By.XPATH, "//p[contains(text(),'Готовы:')]")

        # Счётчик "Выполнено за всё время" после перехода в "Ленту заказов"
        COMPLETED_ORDERS_COUNTER = (By.XPATH, "//p[normalize-space()='153072']")

        # Ингредиент "Флюоресцентная булка R2-D3"
        INGREDIENT_R2D3_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

        # Заголовок с деталями ингредиента при клике на булку
        INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")

        # Крестик для закрытия деталей ингредиента
        CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

        # Цель перетаскивания ингредиента на верхнюю булку
        ORDER_TARGET_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")

        # Счётчик ингредиентов в конструкторе
        INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

        # Кнопка "Оформить заказ"
        PLACE_AN_ORDER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

        # Сообщение об успешном оформлении заказа
        ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")

        # Локатор для заказа в процессе выполнения (шаблон с ID заказа)
        ORDER_IN_PROGRESS_LOCATOR = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[1]//*[contains(text(), '{0}')]")