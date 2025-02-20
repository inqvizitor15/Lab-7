import requests
from pprint import pprint
import json

API_KEY = input('Введите ваш API-ключ, который можно посмотреть в личном кабинете News Api: ')


url_main = 'https://newsapi.org/v2/top-headlines?'

print('Выберите страну, по которой хотите увидеть новость (двухбуквенный код в формате ISO 3166-1)')
country = input('(Если у вас бесплатный тариф, то вы можете выбрать только американский регион (us)): ')

# country = 'us'

category = input('Выберите одну из категорий, по которой хотите увидеть новость (business, entertainment, general, health, science, sports, technology): ' )
# category = 'technology'
page_size = input('Количество новостей, которые вы хотите получить (будет получено на одну меньше): ')
# page_size = 7
print('\n' * 3 + '-' * 34 + 'СВЕЖИЕ НОВОСТИ' + '-' * 33 + '\n')
# URL для запроса к API News Api
url = f"{url_main}country={country}&pageSize={page_size}&apiKey={API_KEY}"
# print(url)

#Отправка GET запроса
response = requests.get(url)

if response.status_code == 200:
    #парсинг
    data = response.json()
    # pprint(data, indent=4)
    for article in data["articles"]:

        print(f"Источник: {article['source']['name']}")
        print(f"Автор: {article.get('author', 'Не указан')}")  # Используем get для обработки отсутствующего автора
        print(f"Заголовок: {article['title']}")
        print(
            f"Описание: {article.get('description', 'Нет описания')}")  # Используем get для обработки отсутствующего описания
        print(f"Дата публикации: {article['publishedAt']}")
        print(f"Ссылка: {article['url']}")
        print("\n" + "$" * 75 + "\n")

else:
    print(f"Ошибка: {response.status_code}")
    print(response.json())  # Вывод сообщения об ошибке
