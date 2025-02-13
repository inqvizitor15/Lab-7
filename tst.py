import requests

# Ваш API-ключ от NewsAPI
API_KEY = "199f68cebfc949cf89cf9166eb0818ff"

# Параметры запроса
country = "us"  # Код страны (например, "us" для США)
page_size = 5   # Количество новостей

# URL для запроса к API NewsAPI
url = f"https://newsapi.org/v2/top-headlines?country={country}&pageSize={page_size}&apiKey={API_KEY}"

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг JSON-ответа
    data = response.json()

    # Вывод структурированной информации
    print('\n' * 3 + '-' * 34 + 'СВЕЖИЕ НОВОСТИ' + '-' * 33 + '\n')
    for article in data["articles"]:
        print(f"Источник: {article['source']['name']}")
        print(f"Автор: {article.get('author', 'Не указан')}")  # Используем get для обработки отсутствующего автора
        print(f"Заголовок: {article['title']}")
        print(f"Описание: {article.get('description', 'Нет описания')}")  # Используем get для обработки отсутствующего описания
        print(f"Дата публикации: {article['publishedAt']}")
        print(f"Ссылка: {article['url']}")
        print("\n" + "=" * 80 + "\n")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())  # Вывод сообщения об ошибке