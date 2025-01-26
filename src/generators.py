from typing import Any, Generator


# Функция принимает на вход список словарей, представляющих транзакции
def filter_by_currency(transactions: list, currency: str = "USD") -> Any:
    """Функция фильтрует транзакции по заданной валюте.Transactions: Список словарей, представляющих транзакции.
    currency: Валюта, по которой будет происходить фильтрация.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


# Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
def transaction_descriptions(transactions: Any) -> Generator:
    """Генератор возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


# Функция генерирующая номер карты в формате XXXX XXXX XXXX XXXX
def card_number_generator(start: int, end: int) -> Generator:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    , где X — цифра номера карты. Генератор может сгенерировать номера карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    for number in range(start, end + 1):
        # приводим номер карты в нормальный вид, по 4 цифры
        card_number = f"{number:0>16}"
        number_news = "".join([card_number[i : i + 4] + " " for i in range(0, 16, 4)])
        yield number_news.strip()
