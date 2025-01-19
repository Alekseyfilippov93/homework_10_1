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
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.

**Пример входных данных для проверки функции**
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`

**Примеры работы функции**
Выход функции со статусом по умолчанию 'EXECUTED'
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]`

2.**Функция sort_by_date**:
Принимает список словарей и необязательный параметр, задающий порядок сортировки 
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)

**Пример входных данных для проверки функции**
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`

**Примеры работы функции**
Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]`

## Тестирование

Тестирование проводиться с помощью простых проверок assert. Если тест не проходит, 
будет подсвечено какой тест не прошел.

**Запуск тестов**

Чтобы запустить тесты, вызовите функции **test_get_mask_card_number**, **test_get_mask_account**,
**test_mask_account_card**, **test_get_date**

## Пример использования

```
def test_get_mask_card_number():
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"
    assert get_mask_card_number("1111111111115555") == "1111 11** **** 5555"

    try:
        get_mask_card_number('566')
        print("Неверный ввод карты")
    except IndexError:
        pass
```
```
def test_get_mask_account():
    assert get_mask_account("64686473678894779589") == "6468 **9589"
    assert get_mask_account("88888888888888888888") == "8888 **8888"

    try:
        get_mask_account('566')
        print("Неверный ввод счета")
    except IndexError:
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
def test_get_date(date_1):
    assert get_date("2024-03-11T02:26:18.671407") == date_1
    try:
        get_date("2024-03-T02:26:18.671407")
        print("День недели отсутствует")
    except IndexError:
        pass
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
**Установка**

Просто импортируйте необходимые функции и запускайте тесты.