# Функция принимает на вход строку формата Visa Platinum 7000792289606361, или Maestro 7000792289606361,
# или Счет 73654108430135874305
from mask import get_mask_account, get_mask_card_number
from typing import Union


def mask_account_card(card: Union[str]) -> str:
    """Определяем счет или номер карты и тип самой карты"""
    if "Visa" or "Maestro" or "MasterCard" in card:
        return get_mask_card_number(card)
    elif "Счет" in card:
        return get_mask_account(card)


card = "Счет 73654108430135874305"
masked_info = mask_account_card(card)
print(masked_info)
