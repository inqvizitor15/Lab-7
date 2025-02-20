import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

# Ваш API-ключ от NASA
API_KEY = input('Введите ваш API-ключ, который можно посмотреть в личном кабинете NASA: ')
# URL для запроса к API NASA
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
    print(f"Фото дня: {title}\n")
    print(f"Описание: {explanation}\n")
    print(f"URL изображения: {image_url}")

    # Загрузка изображения
    if image_url != "Нет URL изображения":
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))

            # Создание окна Tkinter
            root = tk.Tk()
            root.title("NASA IMAGE: " + title)

            # Установка размеров окна (ширина x высота)
            width = 718
            height = 404
            root.geometry(f"{width}x{height}+400+150")

            # Преобразование изображения для Tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Создание метки для отображения изображения
            label = tk.Label(root, image=tk_image)
            label.pack()

            # Создание метки для отображения описания
            desc_label = tk.Label(root, text=explanation, wraplength=400)
            desc_label.pack()

            # Запуск основного цикла Tkinter
            root.mainloop()
        else:
            print("Ошибка при загрузке изображения.")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())  # Вывод сообщения об ошибке