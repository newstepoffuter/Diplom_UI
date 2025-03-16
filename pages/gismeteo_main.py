from selene import browser, have, be
import allure
from dotenv import load_dotenv
import os

load_dotenv()


class TimeoutException:
    pass


class GismeteoUiPage:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL', 'https://www.gismeteo.ru')

    def open(self, path='/'):
        full_url = f"{self.base_url}{path}"
        print(f"Opening URL: {full_url}")
        browser.open(full_url)

    class GismeteoUiPage:
        def search_and_select_city(self, city_name):
            """
            Ищет и выбирает город.
            :param city_name: Название города.
            """
            with allure.step(f'Ищем и выбираем город: {city_name}'):
                try:
                    browser.element('[class="search-form "]').with_(timeout=10).should(be.visible).click()
                    search_input = browser.element('[placeholder="Поиск местоположения"]')
                    search_input.should(be.visible).type(city_name)
                    city_link = browser.element(f'[href*="/weather-{city_name.lower()}"]')
                    city_link.should(be.visible).click()
                except TimeoutException:
                    allure.attach(
                        browser.driver.get_screenshot_as_png(),
                        name=f"search_and_select_city_failed_{city_name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                    raise AssertionError(f"Элемент поиска или город '{city_name}' не найдены")

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

    def gismeteo_title_check_on_app_page(self):
        """
        Проверяет заголовок страницы "Приложения".
        """
        with allure.step('Проверяем заголовок страницы "Приложения"'):
            browser.should(have.title('GISMETEO'))

    def open_moscow(self):
        """
        Открывает страницу с погодой в Москве.
        """
        with allure.step('Открываем страницу с погодой в Москве'):
            self.search_and_select_city('Москва')

    def open_moscow_check(self):
        """
        Проверяет, что открыта страница с погодой в Москве.
        """
        with allure.step('Проверяем, что открыта страница с погодой в Москве'):
            self.verify_city_name('Москва (город федерального значения)')

    def today_weather_title_check(self):
        """
        Проверяет заголовок страницы с погодой на сегодня.
        """
        with allure.step('Проверяем заголовок страницы с погодой на сегодня'):
            self.check_page_title('Погода в Москве сегодня')

    def three_days_weather_title_check(self):
        """
        Проверяет заголовок страницы с погодой на 3 дня.
        """
        with allure.step('Проверяем заголовок страницы с погодой на 3 дня'):
            browser.element('[data-stat-value="3-days"]').click()
            self.check_page_title('Погода в Москве на 3 дня')

    def radar_title_check(self):
        """
        Проверяет заголовок страницы с радаром.
        """
        with allure.step('Проверяем заголовок страницы с радаром'):
            browser.element('[href="/nowcast-moscow-4368/"]').click()
            self.check_page_title('Радар осадков и гроз в Москве')


gismeteo_ui_page = GismeteoUiPage()
