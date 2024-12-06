

# Stellar Burgers UI Tests

Проект по автоматизированному тестированию веб-приложения **Stellar Burgers**. Тесты реализованы с использованием паттерна **Page Object Model** (POM), написаны на Python с использованием **pytest** и **selenium**, а результаты тестирования отображаются в отчетах **Allure**.

**Поддерживаемые браузеры:**
Google Chrome и
Mozilla Firefox
## Структура проекта

Проект состоит из следующих компонентов:

**Директория allure-results_chrome**  
   Используется для хранения результатов тестов для браузера Google Chrome в формате Allure.

**Директория allure-results_firefox**  
   Используется для хранения результатов тестов для браузера Firefox в формате Allure.

**Директория data**  
   Содержит файл `data.py`, в котором хранятся тестовые данные и базовый URL.

**Директория locators**  
   Включает файлы с локаторами элементов страниц

**Директория pages**  
   Реализует паттерн Page Object Model

**Директория tests**  
   Содержит файлы с тестовыми сценариями:
   - `test_account_page.py` - содержит тесты функционала личного кабинета.
   - `test_forgot_password.py` - содержит тесты восстановления пароля.
   - `test_main_page.py` - содержит тесты функционала главной страницы.
   - `test_order_page.py` - содержит тесты ленты заказов.

**Файл conftest.py**  
   Содержит фикстуры для тестов.
**Файл requirements**
  Cодержит зависимости проекта
**Файл config**
  Содержит конфигурациипроекта


1. Установить зависимости из `requirements.txt`:
   ```bash
   pip install -r requirements.txt

# Diplom_3
