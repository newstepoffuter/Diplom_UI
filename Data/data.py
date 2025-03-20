from dataclasses import dataclass


@dataclass
class CityData:
    """
    Класс для хранения данных о городе.
    """
    city_name: str
    expected_city_name: str
    expected_url: str


@dataclass
class CityPageData:
    """
    Класс для хранения данных о странице города.
    """
    city_name: str
    expected_city_name: str


MOSCOW_DATA = CityData(
    city_name='Москва',
    expected_city_name='Москва (город федерального значения)',
    expected_url='/weather-moscow-4368/'
)

SAINT_PETERSBURG_DATA = CityData(
    city_name='Санкт-Петербург',
    expected_city_name='Санкт-Петербург (город федерального значения)',
    expected_url='/weather-saint-petersburg-4079/'
)

MOSCOW_PAGE_DATA = CityPageData(
    city_name='Москва',
    expected_city_name='Москва (город федерального значения)'
)

SAINT_PETERSBURG_PAGE_DATA = CityPageData(
    city_name='Санкт-Петербург',
    expected_city_name='Санкт-Петербург (город федерального значения)'
)
