import allure
import pytest
from pages.ui_check import gismeteo_ui_action


@allure.feature('Базовый UI')
@allure.story("Пользователь видит навигационные кнопки")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка на наличие навигационных кнопок')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI_nav_buttons')
@allure.severity(allure.severity_level.BLOCKER)
def test_nav_buttons():
    gismeteo_ui_action.open('/')
    gismeteo_ui_action.nav_buttons_is_visible()


@allure.feature('Базовый UI')
@allure.story("Пользователь кликает навигационные кнопки")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка на кликабельность навигационных кнопок')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI_nav_buttons')
@allure.severity(allure.severity_level.BLOCKER)
def test_nav_buttons_clickability():
    gismeteo_ui_action.open('/')
    gismeteo_ui_action.nav_buttons_is_clickable()


@allure.feature('Базовый UI')
@allure.story("Пользователь видит навигационные кнопки c текстом")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка наличия текста навигационных кнопок')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI_nav_buttons')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('text', ['Сейчас', 'Сегодня', 'Завтра', '3 дня', '10 дней', '2 недели', 'Месяц', 'Радар'])
def test_nav_text(text):
    gismeteo_ui_action.open('/')
    gismeteo_ui_action.nav_text_is_visible(text)
