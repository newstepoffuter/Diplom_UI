import allure
import pytest
from pages.gismeteo_main import gismeteo_ui_action


@allure.feature('Базовый UI')
@allure.story("Проверка навигационных кнопок")
@allure.link('https://www.gismeteo.ru/')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI_nav_buttons')
class TestNavigationButtons:
    """Тесты для проверки навигационных кнопок на сайте Gismeteo."""

    @pytest.fixture(autouse=True)
    def open_gismeteo(self):
        """Фикстура для открытия главной страницы Gismeteo перед каждым тестом."""
        gismeteo_ui_action.open('/')

    @allure.severity(allure.severity_level.BLOCKER)
    def test_nav_buttons_visibility(self):
        """Проверка, что навигационные кнопки отображаются на странице."""
        gismeteo_ui_action.nav_buttons_is_visible()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_nav_buttons_clickability(self):
        """Проверка, что навигационные кнопки кликабельны."""
        gismeteo_ui_action.nav_buttons_is_clickable()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('text', ['Сейчас', 'Сегодня', 'Завтра', '3 дня', '10 дней', '2 недели', 'Месяц', 'Радар'])
    def test_nav_text_visibility(self, text):
        """Проверка, что навигационные кнопки содержат ожидаемый текст."""
        gismeteo_ui_action.nav_text_is_visible(text)
