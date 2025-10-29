# ...existing code...
def display_weather(city, api_key):
    import requests
    import json
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter OpenWeatherMap API key: ")
    display_weather(city, api_key)
# ...existing code...