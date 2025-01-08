# Функция принимающая список и на выходе получаем список с нужным ключом
def filter_by_state(list_dict: list, state: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    На выходе получаем новый список"""
    new_list_dict = []
# Проверяем есть такой ключ у нас в словаре
    for item in list_dict:
        if item.get('state') == state:
            new_list_dict.append(item)
    return new_list_dict

