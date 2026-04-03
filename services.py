# services.py
# INCOMPATIBLE SERVICES — These are the "legacy" or "3rd-party" classes
# They each return data in completely different formats.
# We CANNOT change these classes (simulating real-world constraints).

class OpenWeatherMapAPI:
    """
    Simulates OpenWeatherMap API.
    Returns data as a nested dictionary with temperature in KELVIN.
    """

    def fetch_data(self, city: str) -> dict:
        # Simulated API responses (real API would use requests + API key)
        mock_data = {
            "Chennai":   {"main": {"temp": 308.15}, "weather": [{"description": "hot and humid"}]},
            "Mumbai":    {"main": {"temp": 305.15}, "weather": [{"description": "partly cloudy"}]},
            "Delhi":     {"main": {"temp": 312.15}, "weather": [{"description": "very hot"}]},
            "Bangalore": {"main": {"temp": 295.15}, "weather": [{"description": "pleasant"}]},
        }
        return mock_data.get(city, {"main": {"temp": 300.00}, "weather": [{"description": "unknown"}]})


class WttrInAPI:
    """
    Simulates wttr.in API.
    Returns data as a plain TEXT string (completely different format!).
    """

    def get_weather_string(self, city: str) -> str:
        # Simulated plain-text responses
        mock_data = {
            "Chennai":   "Weather in Chennai: +35C, Condition: hot and humid",
            "Mumbai":    "Weather in Mumbai: +32C, Condition: partly cloudy",
            "Delhi":     "Weather in Delhi: +39C, Condition: very hot",
            "Bangalore": "Weather in Bangalore: +22C, Condition: pleasant",
        }
        return mock_data.get(city, f"Weather in {city}: +27C, Condition: unknown")


class WeatherXMLService:
    """
    Simulates a legacy XML-based weather service.
    Returns data as an XML string (the most incompatible format!).
    """

    def get_xml_data(self, city: str) -> str:
        mock_data = {
            "Chennai":   "<weather><city>Chennai</city><temp_celsius>35</temp_celsius><desc>hot and humid</desc></weather>",
            "Mumbai":    "<weather><city>Mumbai</city><temp_celsius>32</temp_celsius><desc>partly cloudy</desc></weather>",
            "Delhi":     "<weather><city>Delhi</city><temp_celsius>39</temp_celsius><desc>very hot</desc></weather>",
            "Bangalore": "<weather><city>Bangalore</city><temp_celsius>22</temp_celsius><desc>pleasant</desc></weather>",
        }
        return mock_data.get(city, f"<weather><city>{city}</city><temp_celsius>27</temp_celsius><desc>unknown</desc></weather>")
