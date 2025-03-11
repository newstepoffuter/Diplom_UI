from selene import browser, have, be
import allure


class GismeteoUiPage:
    def open(self, path='/'):
        """
        Открывает сайт Gismeteo.
        :param path: Путь на сайте (по умолчанию открывает главную страницу).
        """
        with allure.step('Открываем сайт Gismeteo'):
            base_url = 'https://www.gismeteo.ru'
            full_url = f"{base_url}{path}"
            browser.open(full_url)

    def search_and_select_city(self, city_name):
        """
        Ищет и выбирает город.
        :param city_name: Название города.
        """
        with allure.step(f'Ищем и выбираем город: {city_name}'):
            browser.element('[placeholder="Поиск местоположения"]').type(city_name)
            browser.element(f'[href*="/weather-{city_name.lower()}"]').click()

    def check_page_title(self, expected_title):
        """
        Проверяет заголовок страницы.
        :param expected_title: Ожидаемый заголовок страницы.
        """
        with allure.step(f'Проверяем заголовок страницы: {expected_title}'):
            browser.element('.page-title').should(have.text(expected_title))

    def verify_city_name(self, expected_city_name):
        """
        Проверяет название города на странице.
        :param expected_city_name: Ожидаемое название города.
        """
        with allure.step(f'Проверяем название города: {expected_city_name}'):
            browser.all('.breadcrumbs-link').second.should(have.text(expected_city_name))

    def nav_buttons_is_visible(self):
        """
        Проверяет видимость навигационных кнопок.
        """
        with allure.step('Проверяем видимость навигационных кнопок'):
            browser.element(".header-nav").should(be.visible)

    def nav_buttons_is_clickable(self):
        """
        Проверяет кликабельность навигационных кнопок.
        """
        with allure.step('Проверяем кликабельность навигационных кнопок'):
            browser.element(".header-nav").should(be.clickable)

    def nav_text_is_visible(self, *button_texts):
        """
        Проверяет наличие текста навигационных кнопок на сайте.
        :param button_texts: Список текстов для проверки.
        """
        with allure.step('Проверяем наличие текста навигационных кнопок на сайте'):
            for text in button_texts:
                browser.element(".header-nav").should(have.text(text))


gismeteo_ui_action = GismeteoUiPage()
