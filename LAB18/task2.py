def display_weather(city, api_key):
    import requests
    import json
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        print(json.dumps(data, indent=2))
    except (requests.exceptions.RequestException, ValueError):
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter OpenWeatherMap API key: ")
    display_weather(city, api_key)