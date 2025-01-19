import pytest
from src.mask import get_mask_card_number
from src.mask import get_mask_account


# Функции для проверки тестов
def test_get_mask_card_number() -> None:
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"
    assert get_mask_card_number("1111111111115555") == "1111 11** **** 5555"
    try:
        get_mask_card_number("566")
        print("Неверный ввод карты")
    except IndexError:
        pass


def test_get_mask_account() -> None:
    assert get_mask_account("64686473678894779599") == "6468 **9599"
    assert get_mask_account("88888888888888888888") == "8888 **8888"
    try:
        get_mask_account("566")
        print("Неверный ввод счета")
    except IndexError:
        pass
