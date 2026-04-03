# adapters.py
# THE ADAPTERS — This is the heart of the pattern.
# Each adapter wraps an incompatible service and translates
# its output to match the WeatherProvider interface.

import xml.etree.ElementTree as ET
from weather_provider import WeatherProvider
from services import OpenWeatherMapAPI, WttrInAPI, WeatherXMLService


class OpenWeatherAdapter(WeatherProvider):
    """
    Adapts OpenWeatherMapAPI (returns dict with Kelvin temps)
    → to WeatherProvider interface (returns Celsius float).
    """

    def __init__(self):
        self._api = OpenWeatherMapAPI()  # Wrapping the incompatible service

    def get_temperature(self, city: str) -> float:
        data = self._api.fetch_data(city)
        kelvin = data["main"]["temp"]
        return round(kelvin - 273.15, 2)   # ADAPTATION: Kelvin → Celsius

    def get_description(self, city: str) -> str:
        data = self._api.fetch_data(city)
        return data["weather"][0]["description"]

    def get_source_name(self) -> str:
        return "OpenWeatherMap API"


class WttrInAdapter(WeatherProvider):
    """
    Adapts WttrInAPI (returns plain text string)
    → to WeatherProvider interface.
    """

    def __init__(self):
        self._api = WttrInAPI()  # Wrapping the incompatible service

    def get_temperature(self, city: str) -> float:
        raw = self._api.get_weather_string(city)
        # ADAPTATION: Parse "Weather in Chennai: +35C, ..." → 35.0
        temp_part = raw.split("+")[1].split("C")[0]
        return float(temp_part)

    def get_description(self, city: str) -> str:
        raw = self._api.get_weather_string(city)
        # ADAPTATION: Parse "...Condition: hot and humid" → "hot and humid"
        return raw.split("Condition: ")[1]

    def get_source_name(self) -> str:
        return "wttr.in API"


class XMLWeatherAdapter(WeatherProvider):
    """
    Adapts WeatherXMLService (returns raw XML string)
    → to WeatherProvider interface.
    """

    def __init__(self):
        self._api = WeatherXMLService()  # Wrapping the incompatible service

    def get_temperature(self, city: str) -> float:
        xml_str = self._api.get_xml_data(city)
        # ADAPTATION: Parse XML → extract temp_celsius
        root = ET.fromstring(xml_str)
        return float(root.find("temp_celsius").text)

    def get_description(self, city: str) -> str:
        xml_str = self._api.get_xml_data(city)
        root = ET.fromstring(xml_str)
        return root.find("desc").text

    def get_source_name(self) -> str:
        return "Legacy XML Service"
