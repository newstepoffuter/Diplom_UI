import allure
import pytest
from selene import browser
from pages.gismeteo_main import gismeteo_ui_page
from data import CityData, CityPageData


@allure.feature('Поиск')
@allure.story("Пользователь ищет город и переходит на страницу с погодой")
@allure.severity(allure.severity_level.CRITICAL)
class TestCitySearch:
    @pytest.mark.parametrize('city_data', [
        CityData(
            city_name='Москва',
            expected_city_name='Москва (город федерального значения)',
            expected_url='/weather-moscow-4368/'
        ),
        CityData(
            city_name='Санкт-Петербург',
            expected_city_name='Санкт-Петербург (город федерального значения)',
            expected_url='/weather-saint-petersburg-4079/'
        ),
    ])
    def test_search_city_and_verify_page(self, city_data):
        """
        Проверяет, что после поиска города пользователь переходит на правильную страницу.
        """
        gismeteo_ui_page.open('/')
        gismeteo_ui_page.search_and_select_city(city_data.city_name)
        assert city_data.expected_url in browser.driver.current_url
        gismeteo_ui_page.verify_city_name(city_data.expected_city_name)


@allure.feature('Данные города')
@allure.story("Пользователь проверяет данные на странице города")
@allure.severity(allure.severity_level.NORMAL)
class TestCityData:
    @pytest.mark.parametrize('city_data', [
        CityPageData(
            city_name='Москва',
            expected_city_name='Москва (город федерального значения)'
        ),
        CityPageData(
            city_name='Санкт-Петербург',
            expected_city_name='Санкт-Петербург (город федерального значения)'
        ),
    ])
    def test_city_data(self, city_data):
        """
        Проверяет, что на странице города отображаются корректные данные.
        """
        gismeteo_ui_page.open(f'/weather-{city_data.city_name.lower()}/')
        gismeteo_ui_page.verify_city_name(city_data.expected_city_name)
        expected_title = f'Погода в {city_data.city_name} сегодня'
        gismeteo_ui_page.check_page_title(expected_title)


@allure.feature('Базовый UI')
@allure.tag('gismeteo_UI')
@allure.label('gismeteo_UI_check')
class TestAppPage:
    """Тесты для проверки страницы 'Приложения'."""

    @allure.story('Пользователь смотрит Title на странице "Приложения"')
    @allure.link('https://www.gismeteo.ru/soft/')
    @allure.description('Проверка наименования Title страницы')
    @allure.severity(allure.severity_level.MINOR)
    def test_check_title_on_app_page(self):
        """Проверка Title страницы 'Приложения'."""
        gismeteo_ui_page.open('soft/')
        gismeteo_ui_page.gismeteo_title_check_on_app_page()


@allure.feature('Поиск')
@allure.tag('gismeteo_UI')
class TestSearch:
    """Тесты для проверки поиска."""

    @allure.story("Пользователь ищет город 'Москва'")
    @allure.link('https://www.gismeteo.ru/')
    @allure.description('Проверка работоспособности поиска')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_check(self):
        """Проверка поиска города 'Москва'."""
        gismeteo_ui_page.open_moscow()
        gismeteo_ui_page.open_moscow_check()


@allure.feature('Базовый UI')
@allure.tag('gismeteo_UI')
@allure.label('gismeteo_UI_check')
class TestWeatherPages:
    """Тесты для проверки страниц с погодой."""

    @pytest.fixture(autouse=True)
    def open_moscow(self):
        """Фикстура для открытия страницы с погодой в Москве перед каждым тестом."""
        gismeteo_ui_page.open_moscow()

    @allure.story("Пользователь смотрит погоду в Москве на сегодня")
    @allure.link('https://www.gismeteo.ru/')
    @allure.description('Проверка корректности наименования на странице города')
    @allure.severity(allure.severity_level.MINOR)
    def test_check_today_weather_title(self):
        """Проверка заголовка страницы с погодой на сегодня."""
        gismeteo_ui_page.today_weather_title_check()

    @allure.story("Пользователь смотрит погоду в Москве на 3 дня")
    @allure.link('https://www.gismeteo.ru/')
    @allure.description('Проверка корректности наименования на странице города')
    @allure.severity(allure.severity_level.MINOR)
    def test_check_3_days_weather_title(self):
        """Проверка заголовка страницы с погодой на 3 дня."""
        gismeteo_ui_page.three_days_weather_title_check()

    @allure.story("Пользователь смотрит радар по Москве")
    @allure.link('https://www.gismeteo.ru/')
    @allure.description('Проверка корректности наименования на странице города')
    @allure.severity(allure.severity_level.NORMAL)
    def test_check_radar(self):
        """Проверка заголовка страницы с радаром."""
        gismeteo_ui_page.radar_title_check()
