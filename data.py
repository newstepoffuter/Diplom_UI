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
