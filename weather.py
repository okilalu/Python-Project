import requests

API_KEY = "f493235022f117443717201d55ff1d93"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name : ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temprature = round(data['main']['temp'] - 273.15, 2)
    print("Weather: ", weather)
    print("Temprature: ",temprature, "Celcius: ")
else:
    print("An error occured")