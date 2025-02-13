import requests
import json
# Ваш API-ключ от OpenWeatherMap
API_KEY = "d4b8729805537956569f2a16003f293c"

# Название города
city_name = "Moscow"

# URL для запроса к API OpenWeatherMap
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг JSON-ответа
    data = response.json()
    data_json = json.dumps(data, indent=4)

    print(type(data_json))
    print(data_json)
    # weather = data_json["weather"]["description"]
#     # Извлечение данных о погоде
#     weather = data["weather"][0]["description"]
#     temperature = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     pressure = data["main"]["pressure"]
#
#     # Вывод результатов
    print(f"Погода в городе {city_name}:")
#     print(f"Температура: {temperature}°C")
#     print(f"Влажность: {humidity}%")
#     print(f"Давление: {pressure} hPa")
    print(f"Описание: {weather.capitalize()}")
# else:
#     print(f"Ошибка: {response.status_code}")
#     print(response.json())  # Вывод сообщения об ошибке
