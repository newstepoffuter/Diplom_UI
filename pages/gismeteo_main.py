from selene import browser, have, be
import allure
from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()


class GismeteoUiPage:
    def __init__(self):
        # Получаем BASE_URL из переменных окружения
        self.base_url = os.getenv('BASE_URL')

    def open(self, path='/'):
        """
        Открывает сайт Gismeteo.
        :param path: Путь на сайте (по умолчанию открывает главную страницу).
        """
        with allure.step(f'Открываем страницу: {path}'):
            full_url = f"{self.base_url}{path}"
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


# Создаем экземпляр класса для использования в тестах
gismeteo_ui_page = GismeteoUiPage()
