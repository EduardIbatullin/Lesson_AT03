import pytest
from lw_AT03_2 import get_github_user


def test_get_github_user(mocker):
    mock_get = mocker.patch('lw_AT03_2.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nikita',
    }
    user_data = get_github_user('nizavr')
    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nikita',
    }


def test_get_github_user_fail(mocker):
    mock_get = mocker.patch('lw_AT03_2.requests.get')
    mock_get.return_value.status_code = 500

    user_data = get_github_user('nizavr')
    assert user_data == None
