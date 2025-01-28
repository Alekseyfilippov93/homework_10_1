from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
import pytest


# Функции для проверки тестов
def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    usd_transactions_1 = filter_by_currency(transactions, "RUB")
    assert usd_transactions == usd_transactions
    assert usd_transactions != usd_transactions_1


@pytest.mark.parametrize(
    "currency, expected",
    [
        # кортеж данных для первого теста
        (
                "USD",
                [
                    {
                        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод организации",
                    },
                    {
                        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод со счета на счет",
                    },
                    {
                        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Перевод с карты на карту",
                    },
                ],
        ),
        # кортеж данных для второго теста
        (
                "RUB",
                [
                    {
                        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод со счета на счет",
                    },
                    {
                        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                    },
                ],
        ),
        # кортеж данных для третьего теста
        ("EUR", []),
    ],
)
def test_1_filter_by_currency(transactions, currency, expected):
    assert list(filter_by_currency(transactions, currency)) == expected


# Функции для проверки тестов
def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    # Проверка пустого списка


def test_transactions_empty():
    descriptions = list(transaction_descriptions([]))
    assert descriptions == [], "Ошибка: должен быть пустой результат"


def test_card_number_generator():
    card_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
    ]
    card_numbers_new = list(card_number_generator(1, 6))
    assert card_numbers_new == card_numbers

    # Проверка крайних значений диапазона
    assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]
    assert list(card_number_generator(6, 6)) == ["0000 0000 0000 0006"]
    assert list(card_number_generator(7, 7)) == ["0000 0000 0000 0007"]
