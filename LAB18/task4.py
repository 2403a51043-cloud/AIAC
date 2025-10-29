def display_weather_details(city, api_key):
    import requests
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        resp.raise_for_status()
        data = resp.json()
        name = data.get('name', city)
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"City: {name}")
        print(f"Temperature: {int(round(temp))}°C")
        print(f"Humidity: {int(round(humidity))}%")
        print(f"Weather: {description.capitalize()}")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter OpenWeatherMap API key: ")
    display_weather_details(city, api_key)