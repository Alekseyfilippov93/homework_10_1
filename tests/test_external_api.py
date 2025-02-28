from unittest.mock import patch, Mock
from src.external_api import get_exchange_rate, convert_rub


def test_get_exchange_rate_success():
    """
    Тест на успешное получение курса валюты.
    """
    # Мокируем успешный ответ от API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 88.0}}

    with patch("requests.get", return_value=mock_response):
        rate = get_exchange_rate("USD")
        assert rate == 88.0


def test_convert_rub():
    """
    Тест на конвертацию суммы в рублях (RUB).
    """
    transaction = {"amount": 100.0, "currency": "RUB"}
    result = convert_rub(transaction)
    assert result == 100.0
