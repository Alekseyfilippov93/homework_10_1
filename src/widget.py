from mask import get_mask_card_number, get_mask_account
from typing import Union


# Функция принимает на вход строку формата Visa Platinum 7000792289606361, или Maestro 7000792289606361,
# или Счет 73654108430135874305
def mask_account_card(card: Union[str]) -> str:
    """Определяем счет или номер карты и тип самой карты"""
    if "Visa" or "Maestro" or "MasterCard" in card:
        return get_mask_card_number(card)
    elif "Счет" in card:
        return get_mask_account(card)


if __name__ == "__main__":
    print(mask_account_card("Visa 8990922113665229"))
    print(get_mask_account("Счет 64686473678894779589"))
