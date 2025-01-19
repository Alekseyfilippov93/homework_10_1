from src.widget import mask_account_card
from src.widget import get_date
import pytest


# Функции для проверки тестов
@pytest.mark.parametrize(
    "card, result_1",
    [
        ("Счет 73654108430135874305", "Счет 7365 **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(card, result_1):
    assert mask_account_card(card) == result_1


def test_get_date(date_1):
    assert get_date("2024-03-11T02:26:18.671407") == date_1
    try:
        get_date("2024-03-T02:26:18.671407")
        print("День недели отсутствует")
    except IndexError:
        pass
