from selene import browser, have, be
import allure


class GismeteoUiPagesCheck:

    def open(self, address=''):
        with allure.step('Открываем сайт gismeteo'):
            browser.open(address)

    def moscow_choise(self):
        with allure.step('Выбираем "Москву"'):
            browser.element('[placeholder="Поиск местоположения"]').type('Москва')
            browser.element('[href="/weather-moscow-4368/"]').click()

    def gismeteo_title_check_on_app_page(self):
        with allure.step('Проверяем Title страницы'):
            browser.should(have.title('GISMETEO'))

    def today_weather_title_check(self):
        with allure.step('Проверяем наименование на странице города. "Погода в Москве сегодня"'):
            browser.element('.page-title').should(have.text('Погода в Москве сегодня'))

    def three_days_weather_title_check(self):
        with allure.step('Проверяем наименование на странице города."Погода в Москве на 3 дня"'):
            browser.element('[data-stat-value="3-days"]').click()
            browser.element('.page-title').should(have.text('Погода в Москве на 3 дня'))

    def radar_title_check(self):
        with allure.step('Проверяем наименование на странице города."Радар осадков и гроз в Москве"'):
            browser.element('[href="/nowcast-moscow-4368/"]').click()
            browser.element('.page-title').should(have.text('Радар осадков и гроз в Москве'))

    def open_moscow(self):
        with allure.step('Ищем город "Москва" через поиск'):
            self.open()
            self.moscow_choise()

    def open_moscow_check(self):
        with allure.step('Проверяем наименование города - Москва'):
            browser.all('.breadcrumbs-link').second.should(have.text('Москва (город федерального значения)'))

    def nav_buttons_is_visible(self):
        with allure.step('Проверяем наличие навигационого блока на сайте'):
            browser.element(".header-nav").should(be.visible)

    def nav_buttons_is_clickable(self):
        with allure.step('Проверяем кликабельность навигационого блока на сайте'):
            browser.element(".header-nav").should(be.clickable)

    def nav_text_is_visible(self, button_text):
        with allure.step('Проверяем наличие текста навигационных кнопок на сайте'):
            browser.element(".header-nav").should(have.text(f'{button_text}'))


gismeteo_ui_action = GismeteoUiPagesCheck()