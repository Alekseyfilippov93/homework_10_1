# Функция принимает на вход список словарей, представляющих транзакции
def filter_by_currency(transactions, currency):
    """Функция фильтрует транзакции по заданной валюте.Transactions: Список словарей, представляющих транзакции.
    currency: Валюта, по которой будет происходить фильтрация.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)


# Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
def transaction_descriptions(transactions):
    """Генератор возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for transaction in range(2):
    print(next(descriptions))
    pass


# Функция генерирующая номер карты в формате XXXX XXXX XXXX XXXX
def card_number_generator(start, end):
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    , где X — цифра номера карты. Генератор может сгенерировать номера карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    for number in range(start, end + 1):
        # приводим номер карты в нормальный вид, по 4 цифры
        card_number = f"{number:0>16}"
        number_news = "".join([card_number[i : i + 4] + " " for i in range(0, 16, 4)])
        yield number_news.strip()


for card_number in card_number_generator(1, 6):
    print(card_number)
