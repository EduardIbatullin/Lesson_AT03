import requests


def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"

    try:
        # Отправляем GET-запрос к TheCatAPI для получения случайного изображения кошки
        response = requests.get(url)

        # Если запрос успешен, возвращаем URL изображения
        if response.status_code == 200:
            data = response.json()  # Преобразуем ответ в JSON
            return data[0]['url']  # Возвращаем URL первой картинки

        # Если запрос неуспешен, возвращаем None
        else:
            return None

    # Обрабатываем возможные ошибки запроса, возвращаем None в случае ошибки
    except requests.RequestException:
        return None
