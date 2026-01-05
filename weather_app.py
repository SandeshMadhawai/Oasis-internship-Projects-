import requests # type: ignore

API_KEY = "4762572f28e1eefc81a12f356e42d1ad"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)


    if response.status_code == 200:
        data = response.json()

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        wind = data['wind']['speed']

        print("\nWeather Report")
        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition.capitalize())
        print("Wind Speed:", wind, "m/s")
    else:
        print("City not found.")

def main():
    city = input("Enter city name: ")
    get_weather(city)

main()
