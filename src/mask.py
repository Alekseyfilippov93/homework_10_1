from typing import Union


# Функция принимающая номер карты, и возврашает ее маску
def get_mask_card_number(numbers: Union[str]) -> Union[str]:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    new_mask_card = numbers[0:-12] + " " + numbers[11:13] + "** **** " + numbers[-4:]
    return new_mask_card


# Функцию маскировки номера банковского счета
def get_mask_account(mask_account: Union[str]) -> Union[str]:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"""
    new_mask_account = mask_account[:4] + " " + "**" + mask_account[-4:]
    return new_mask_account


if __name__ == "__main__":
    print(get_mask_card_number("maestro 8990922113665229"))
    print(get_mask_account("счет 64686473678894779589"))
