from mask import get_mask_card_number, get_mask_account
from typing import Union


# Функция принимает на вход строку формата Visa Platinum 7000792289606361, или Maestro 7000792289606361,
# или Счет 73654108430135874305
def mask_account_card(card: Union[str]) -> str:
    """Определяем счет или номер карты и тип самой карты"""
    if "Visa" or "Maestro" or "MasterCard" in card:
        return get_mask_card_number(card)
    elif "Счет" in card:
        return "Счет" + "**" + get_mask_account(card[5:0])


# Функция принимает дату и преобразовывает её
def get_date(date_str: str) -> str:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")."""
    date_new = date_str[8:10] + "." + date_str[5:7] + "." + date_str[0:4]
    return date_new


if __name__ == "__main__":
    print(mask_account_card("Visa 8990922113665229"))
    print(get_mask_account("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
