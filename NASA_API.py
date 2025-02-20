import requests
import tensorflow
from pillow import Image
from io import BytesIO

# Ваш API-ключ от NASA
API_KEY = "hS5DIqhGneMKQHCxJy9a4ZDEKccz088YRkYPcbzG"

# URL для запроса к API NASA APOD
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг JSON-ответа
    data = response.json()

    # Извлечение данных
    title = data.get("title", "Нет заголовка")
    explanation = data.get("explanation", "Нет описания")
    image_url = data.get("url", "Нет URL изображения")

    # Вывод информации
    print(f"Фото дня (APOD): {title}\n")
    print(f"Описание: {explanation}\n")
    print(f"URL изображения: {image_url}")

    # Загрузка и отображение изображения
    if image_url != "Нет URL изображения":
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image.show()
        else:
            print("Ошибка при загрузке изображения.")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())  # Вывод сообщения об ошибке