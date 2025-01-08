# Функция принимающая список и на выходе получаем список с нужным ключом
def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    На выходе получаем новый список"""
    new_list_dict = []
    # Проверяем есть такой ключ у нас в словаре
    for item in list_dict:
        if item.get("state") == state:
            new_list_dict.append(item)
    return new_list_dict


# Функция, которая сортирует по дате словари
def sort_by_date(list_dict: list, sorting: bool = True) -> list:
    """Функция принимает список словарей и сортирует по умолчанию - убывание."""
    # Сортируем список по ключу date
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=sorting)
    return sorted_list
