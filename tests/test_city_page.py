import allure
import pytest
from selene import browser
from pages.gismeteo_main import gismeteo_ui_page
from Data.data import MOSCOW_DATA, SAINT_PETERSBURG_DATA, MOSCOW_PAGE_DATA, SAINT_PETERSBURG_PAGE_DATA


@allure.feature('Поиск')
@allure.story("Пользователь ищет город и переходит на страницу с погодой")
@allure.severity(allure.severity_level.CRITICAL)
class TestCitySearch:
    @pytest.mark.parametrize('city_data', [MOSCOW_DATA, SAINT_PETERSBURG_DATA])
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
    @pytest.mark.parametrize('city_data', [MOSCOW_PAGE_DATA, SAINT_PETERSBURG_PAGE_DATA])
    def test_city_data(self, city_data):
        """
        Проверяет, что на странице города отображаются корректные данные.
        """
        gismeteo_ui_page.open(f'/weather-{city_data.city_name.lower()}/')
        gismeteo_ui_page.verify_city_name(city_data.expected_city_name)
        expected_title = f'Погода в {city_data.city_name} сегодня'
        gismeteo_ui_page.check_page_title(expected_title)
