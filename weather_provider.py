# weather_provider.py
# CLIENT INTERFACE — All adapters must follow this contract

from abc import ABC, abstractmethod

class WeatherProvider(ABC):
    """
    The Target Interface.
    All adapters implement this so the client code
    never needs to know WHICH service it's talking to.
    """

    @abstractmethod
    def get_temperature(self, city: str) -> float:
        """Return temperature in Celsius."""
        pass

    @abstractmethod
    def get_description(self, city: str) -> str:
        """Return a short weather description."""
        pass

    @abstractmethod
    def get_source_name(self) -> str:
        """Return the name of the data source."""
        pass
