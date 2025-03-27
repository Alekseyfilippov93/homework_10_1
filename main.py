import os
from config import DATA_DIR
from src.processing import filter_by_state
from src.reading_financial_transactions import read_csv, read_excel
from src.search_using_regular_expressions import filter_transactions_by_description
from src.utils import load_operation_json
from src.widget import get_date, mask_account_card


def format_transaction(transaction):
    """Форматирует транзакцию для вывода"""
    amount = transaction.get("amount") or transaction.get("operationAmount")["amount"]
    currency_out = transaction.get("currency_name") or transaction.get("operationAmount")["currency"]["name"]
    if transaction.get("from") and transaction.get("from") != "nan":
        print(
            "\n"
            f"{get_date(transaction.get('date'))} {transaction.get('description')}\n"
            f"{mask_account_card(transaction.get('from'))} -> {mask_account_card(transaction.get('to'))}\n"
            f"Сумма: {amount} {currency_out}"
        )
    else:
        print(
            "\n"
            f"{get_date(transaction.get('date'))} {transaction.get('description')}\n"
            f"{mask_account_card(transaction.get('to'))}\n"
            f"Сумма: {amount} {currency_out}"
        )


def main():
    """Отвечает за основную логику проекта и связывает функции между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # 1. Выбор файла пользователя
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    if choice == "1":
        file_path = os.path.join(DATA_DIR, "operations.json")
        transactions = load_operation_json(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = os.path.join(DATA_DIR, "transactions.csv")
        transactions = read_csv(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        transactions = read_excel(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    # 2. Фильтрация по статусу
    stata = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )
        if state in stata:
            print(f'Операции отфильтрованы по статусу "{state}"')
            filtered_transactions = filter_by_state(transactions, state)
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    # 3. Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == "да":
        order_choice = input("Сортировать по возрастанию или по убыванию?\n").strip().lower()
        if order_choice == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x["date"])
        elif order_choice == "по убыванию":
            filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if currency_choice == "да":
        filtered_transactions = [
            t
            for t in filtered_transactions
            if "currency_code" in t
            and t["currency_code"] == "RUB"
            or "operationAmount" in t
            and t["operationAmount"]["currency"]["code"] == "RUB"
        ]

    description_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    )
    if description_filter == "да":
        search_string = input("Введите строку для поиска в описании: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    # 6. Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            format_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
