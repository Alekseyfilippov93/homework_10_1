from typing import Union


# Функция принимающая номер карты, и возврашает ее маску
def get_mask_card_number(numbers: Union[str]) -> Union[str]:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if len(numbers) != 16:
        raise ValueError("Неверный ввод карты. Номер карты состоит из 16 чисел")
    # new_mask_card = numbers[0:-12] + " " + numbers[-12:-10] + "** **** " + numbers[-4:]
    return f"{numbers[:4]} {numbers[4:6]}** **** {numbers[12:]}"


# Функцию маскировки номера банковского счета
def get_mask_account(mask_account: Union[str]) -> Union[str]:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"""
    new_mask_account = mask_account[:4] + " " + "**" + mask_account[-4:]
    return new_mask_account


if __name__ == "__main__":
    print(get_mask_card_number("6468647367889477"))
    print(get_mask_account("64686473678894779589"))
