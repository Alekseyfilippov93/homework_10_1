# Виджет по банковским операциям клиента

## Описание:

Виджет - помогает найти банковские операции по заданным параметрам

## Инструкции по установке:

1. Выполнить клонирование репозитория с github homework_10_1.
2. В терминале, находясь в корневой папке проекта, активировать виртуальное окружение через poetry.
3. Установить все зависимости.

## Использование разработанных функций

1. **Функция filter_by_state**:
   Принимает список словарей и опционально значение для ключа
   state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых
   ключ
   state соответствует указанному значению.

**Пример входных данных для проверки функции**

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

**Примеры работы функции**
Выход функции со статусом по умолчанию 'EXECUTED'

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

2.**Функция sort_by_date**:
Принимает список словарей и необязательный параметр, задающий порядок сортировки
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)

**Пример входных данных для проверки функции**

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

**Примеры работы функции**
Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

## Тестирование

Тестирование проводиться с помощью простых проверок assert. Если тест не проходит,
будет подсвечено какой тест не прошел.

**Запуск тестов**

Чтобы запустить тесты, вызовите функции **test_get_mask_card_number**, **test_get_mask_account**,
**test_mask_account_card**, **test_get_date**, **test_filter_by_currency**, **test_transaction_descriptions**,
**test_card_number_generator**

## Пример использования

```
def test_get_mask_card_number():
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"
    assert get_mask_card_number("7861315131235651") == "7861 31** **** 5651"
    try:
        get_mask_card_number("44648")
    except ValueError as error:
        print(error)
```

```
def test_get_mask_account():
    assert get_mask_account("64686473678894779599") == "6468 **9599"
    assert get_mask_account("88888888888888888888") == "8888 **8888"
    try:
        get_mask_account("566")
        print("Неверный ввод счета")
    except ValueError:
        pass
```

```
@pytest.mark.parametrize(
    "card, result_1",
    [
        ("Счет 73654108430135874305", "Счет 7365 **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(card, result_1):
    assert mask_account_card(card) == result_1
```

```
ef test_get_date(date_1):
    assert get_date("2024-03-11T02:26:18.671407") == date_1
    try:
        get_date("T02:26:18.671")
    except ValueError as error:
        print(error)
```

```
def test_filter_by_state(dict_1):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == dict_1
    )
```

```
@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            [{"date": "2023-01-01"}, {"date": "2022-01-01"}, {"date": "2024-01-01"}],
            [{"date": "2024-01-01"}, {"date": "2023-01-01"}, {"date": "2022-01-01"}],
        ),
        # Тесты на одинаковые даты
        (
            [{"date": "2022-01-01", "name": "A"}, {"date": "2022-01-01", "name": "B"}],
            [{"date": "2022-01-01", "name": "A"}, {"date": "2022-01-01", "name": "B"}],
        ),
    ],
)
def test_sort_by_date(input_data, expected_output):
    assert sort_by_date(input_data) == expected_output
```
```
def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    usd_transactions_1 = filter_by_currency(transactions, "RUB")
    assert usd_transactions == usd_transactions
    assert usd_transactions != usd_transactions_1 
```
```
def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    
    # Проверка пустого списка
    descriptions = list(transaction_descriptions([]))
    assert descriptions == [], "Ошибка: Нет данных"
```
```
def test_card_number_generator():
    card_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
    ]
    card_numbers_new = list(card_number_generator(1, 6))
    assert card_numbers_new == card_numbers

    # Проверка крайних значений диапазона
    assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]
    assert list(card_number_generator(6, 6)) == ["0000 0000 0000 0006"]
    assert list(card_number_generator(7, 7)) == ["0000 0000 0000 0007"]
```

**Установка**

Просто импортируйте необходимые функции и запускайте тесты.

### Использование функций из модуля generators.py

1. **Функция filter_by_currency**
   Функция фильтрует транзакции по заданной валюте.
   Transactions: Список словарей, представляющих транзакции.
   currency: Валюта, по которой будет происходить фильтрация

**Пример использования**

```
def filter_by_currency(transactions, currency):
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
```

**Результат функции**

```
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
```

2. **Функция transaction_descriptions**
   Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди

**Пример использования**

```
def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]
        
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
descriptions = transaction_descriptions(transactions)
for transaction in range(2):
    print(next(descriptions))
```

**Результат функции**

```
Перевод организации
Перевод со счета на счет cебе
```

3.**Функция card_number_generator**

Функция генерирующая номер карты в формате XXXX XXXX XXXX XXXX
где X — цифра номера карты. Генератор может сгенерировать номера карт в
заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999

**Пример использования**

```
def card_number_generator(start, end):
    for number in range(start, end + 1):
        # приводим номер карты в нормальный вид, по 4 цифры
        card_number = f"{number:0>16}"
        number_news = "".join([card_number[i: i + 4] + " " for i in range(0, 16, 4)])
        yield number_news.strip()


for card_number in card_number_generator(1, 6):
    print(card_number)
```

**Результат функции**

```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
0000 0000 0000 0006
```

