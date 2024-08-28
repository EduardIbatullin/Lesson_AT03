import pytest
from lw_AT03_1 import get_weather


def test_get_weather(mocker):
    mock_get = mocker.patch('lw_AT03_1.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 20}
    }

    api_key = 'your_api_key'
    city = 'London'
    weather = get_weather(api_key, city)
    assert weather == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 20}
    }


def test_get_weather_error(mocker):
    mock_get = mocker.patch('lw_AT03_1.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'your_api_key'
    city = 'London'
    weather = get_weather(api_key, city)
    assert weather == None
