def display_weather_details(city, api_key):
    import requests
    import json
    import os

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        resp.raise_for_status()
        data = resp.json()

        name = data.get('name', city)
        temp = int(round(data['main']['temp']))
        humidity = int(round(data['main']['humidity']))
        description = data['weather'][0]['description'].capitalize()

        # Console output (user-friendly)
        print(f"City: {name}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

        # Prepare JSON record and append to results.json in current directory
        record = {"city": name, "temp": temp, "humidity": humidity, "weather": description}
        file_path = os.path.join(os.getcwd(), "results.json")

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    existing = json.load(f)
                    if not isinstance(existing, list):
                        existing = []
            except (json.JSONDecodeError, ValueError):
                existing = []
        else:
            existing = []

        existing.append(record)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter OpenWeatherMap API key: ")
    display_weather_details(city, api_key)