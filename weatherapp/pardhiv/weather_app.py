import requests
from datetime import datetime

API_KEY = "141d40fb5563de03095c12e8738c8805"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 404:
            print("❌ City not found.")
            return None

        if response.status_code == 401:
            print("❌ Invalid API key.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"❌ Error: {error}")
        return None


def save_search_history(city):
    """Save searched cities to a file."""

    with open("search_history.txt", "a", encoding="utf-8") as file:
        file.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {city}\n"
        )


def display_weather(data):
    """Display formatted weather information."""

    print("\n" + "=" * 55)
    print(f"{'WEATHER REPORT':^55}")
    print("=" * 55)

    print(
        f"Date & Time : "
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )
    print(f"Location    : {data['name']}, {data['sys']['country']}")
    print(
        f"Condition   : "
        f"{data['weather'][0]['description'].title()}"
    )
    print(f"Temperature : {data['main']['temp']}°C")
    print(f"Feels Like  : {data['main']['feels_like']}°C")
    print(f"Humidity    : {data['main']['humidity']}%")
    print(f"Pressure    : {data['main']['pressure']} hPa")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")

    print("=" * 55)


def main():
    print("\n🌦️ Welcome to the Weather Application")
    print("-" * 40)

    while True:
        city = input(
            "\nEnter city name (or type 'exit' to quit): "
        ).strip()

        if city.lower() == "exit":
            print("\nThank you for using the Weather App!")
            break

        if not city:
            print("⚠️ Please enter a valid city name.")
            continue

        weather_data = get_weather(city)

        if weather_data:
            display_weather(weather_data)
            save_search_history(city)


if __name__ == "__main__":
    main()
