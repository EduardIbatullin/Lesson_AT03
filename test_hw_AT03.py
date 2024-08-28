import pytest
import requests
from unittest.mock import patch
from hw_AT03 import get_random_cat_image


def test_get_random_cat_image_success():
    # Мокированные данные для успешного ответа от TheCatAPI
    mock_response_data = [{
        "id": "abc123",
        "url": "https://cdn2.thecatapi.com/images/abc123.jpg"
    }]

    # Патчируем метод requests.get для имитации успешного запроса
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200  # Устанавливаем успешный статус код
        mock_get.return_value.json.return_value = mock_response_data  # Возвращаем мокированные данные

        result = get_random_cat_image()

        # Проверяем, что функция вернула правильный URL
        assert result == "https://cdn2.thecatapi.com/images/abc123.jpg"


def test_get_random_cat_image_failure():
    # Патчируем метод requests.get для имитации неуспешного запроса
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404  # Устанавливаем статус код 404

        result = get_random_cat_image()

        # Проверяем, что функция вернула None
        assert result is None


def test_get_random_cat_image_exception():
    # Патчируем метод requests.get, чтобы выбросить исключение RequestException
    with patch('requests.get', side_effect=requests.RequestException):
        result = get_random_cat_image()

        # Проверяем, что функция вернула None
        assert result is None
