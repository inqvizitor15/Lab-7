import requests
from pprint import pprint
import json

API_KEY = input('Введите ваш API-ключ, который можено посмотреть в личном кабинете OpenWeatherMap: ')

# Название города
city_name = input('Введите название города, для которого вы хотите узнать погоду (на Англ. яз.): ')

# URL для запроса к API OpenWeatherMap
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг JSON-ответа
    data = response.json()
    # print(data)
    # pprint(data, indent=4)

    # Извлечение данных о погоде
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

     # Вывод результатов
    print(f"Погода в городе {city_name}:")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Описание: {weather.capitalize()}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())  # Вывод сообщения об ошибке
