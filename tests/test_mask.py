from src.mask import get_mask_account
from src.mask import get_mask_card_number
import pytest


# Функции для проверки тестов
def test_get_mask_card_number():
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"
    assert get_mask_card_number("7861315131235651") == "7861 31** **** 5651"
    try:
        get_mask_card_number("44648")
    except ValueError as error:
        print(error)


def test_get_mask_account():
    assert get_mask_account("64686473678894779599") == "6468 **9599"
    assert get_mask_account("88888888888888888888") == "8888 **8888"
    try:
        get_mask_account("566")
        print("Неверный ввод счета")
    except ValueError:
        pass
