def display_weather_details(city, api_key):
    import requests
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    name = data['name']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    print(f"City: {name}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description.capitalize()}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter OpenWeatherMap API key: ")
    display_weather_details(city, api_key)