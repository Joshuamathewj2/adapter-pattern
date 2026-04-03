# main.py
# CLIENT CODE — Uses only the WeatherProvider interface.
# It has NO idea what's happening inside each adapter.
# This is the whole point of the Adapter Pattern!

from adapters import OpenWeatherAdapter, WttrInAdapter, XMLWeatherAdapter

def display_weather(provider, city: str):
    """
    Client function — works with ANY WeatherProvider.
    Doesn't care if it's XML, JSON, plain text behind the scenes.
    """
    temp = provider.get_temperature(city)
    desc = provider.get_description(city)
    source = provider.get_source_name()
    print(f"  📍 {city}")
    print(f"  🌡️  Temperature : {temp}°C")
    print(f"  🌤️  Condition   : {desc}")
    print(f"  🔌 Source      : {source}")
    print()


if __name__ == "__main__":
    cities = ["Chennai", "Mumbai", "Delhi", "Bangalore"]

    # Three completely different services — same interface!
    providers = [
        OpenWeatherAdapter(),   # Wraps JSON/dict API
        WttrInAdapter(),        # Wraps plain text API
        XMLWeatherAdapter(),    # Wraps legacy XML API
    ]

    print("=" * 50)
    print("   🌦️  WEATHER AGGREGATOR — Adapter Pattern")
    print("=" * 50)

    for provider in providers:
        print(f"\n── Using: {provider.get_source_name()} ──\n")
        for city in cities:
            display_weather(provider, city)

    print("=" * 50)
    print("✅ Same client code. 3 incompatible services.")
    print("   That's the Adapter Pattern.")
    print("=" * 50)
