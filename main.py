import re
from typing import List, Dict
from src.processing import filter_by_state, sort_by_date
from src.reading_financial_transactions import read_csv, read_excel
from src.search_using_regular_expressions import filter_transactions_by_description, count_transactions_by_category
from src.utils import load_operation_json


def format_transaction(transaction: Dict) -> str:
    """Форматирование транзакции для вывода с учетом вашего формата данных"""
    lines = []

    # Дата (конвертация из ISO формата)
    if 'date' in transaction:
        date_str = transaction['date'][:10]  # Берем только дату без времени
        lines.append(date_str)

    # Описание
    if 'description' in transaction:
        lines.append(transaction['description'])

    # Откуда (с маскировкой)
    if 'from' in transaction:
        from_str = transaction['from']
        masked_from = re.sub(r'(\d{4})(\d{2})\d+(\d{4})', r'\1**\3', from_str)
        lines.append(f"From: {masked_from}")

    # Куда (с маскировкой)
    if 'to' in transaction:
        to_str = transaction['to']
        masked_to = re.sub(r'(\d{4})(\d{2})\d+(\d{4})', r'\1**\3', to_str)
        lines.append(f"To: {masked_to}")

    # Сумма и валюта
    if 'amount' in transaction and 'currency_name' in transaction:
        lines.append(f"Amount: {transaction['amount']} {transaction['currency_name']}")

    return "\n".join(lines) + "\n" + "-" * 40


def get_valid_input(prompt: str, validator, error_msg: str):
    """Получает валидный ввод от пользователя"""
    while True:
        user_input = input(prompt).strip()
        if validator(user_input):
            return user_input
        print(error_msg)


def get_valid_status_input(valid_statuses: List[str]) -> str:
    """Получение статуса от пользователя с регистронезависимой проверкой"""
    while True:
        status = input(f"Введите статус ({', '.join(valid_statuses)}): ").strip()
        if any(status.lower() == s.lower() for s in valid_statuses):
            return next(s for s in valid_statuses if s.lower() == status.lower())
        print(f"Ошибка: статус '{status}' недопустим. Попробуйте снова.")


def filter_transactions_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Обертка для filter_by_state с регистронезависимой фильтрацией"""
    # Сначала пробуем стандартный вызов
    filtered = filter_by_state(transactions, status.upper())

    # Если не найдено, пробуем регистронезависимый поиск
    if not filtered:
        filtered = [t for t in transactions
                    if 'state' in t and t['state'].lower() == status.lower()]

    return filtered


def main():
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")

    try:
        # 1. Выбор и загрузка файла
        print("\nВыберите тип файла:")
        print("1. JSON")
        print("2. CSV")
        print("3. XLSX")
        file_type = get_valid_input(
            "Ваш выбор (1-3): ",
            lambda x: x in ['1', '2', '3'],
            "Неверный выбор. Введите 1, 2 или 3"
        )

        file_path = input("Введите путь к файлу: ").strip()

        if file_type == "1":
            transactions = load_operation_json(file_path)
            print("\nДля обработки выбран JSON-файл.")
        elif file_type == "2":
            transactions = read_csv(file_path)
            print("\nДля обработки выбран CSV-файл.")
        elif file_type == "3":
            transactions = read_excel(file_path)
            print("\nДля обработки выбран XLSX-файл.")

        if not transactions:
            print("Файл не содержит данных или произошла ошибка чтения.")
            return

        # 2. Фильтрация по статусу (регистронезависимая)
        valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
        status = get_valid_status_input(valid_statuses)

        transactions = filter_transactions_by_status(transactions, status)
        print(f"\nОперации отфильтрованы по статусу '{status.upper()}'")

        if not transactions:
            print("Не найдено ни одной транзакции с указанным статусом.")
            return

        # 3. Сортировка по дате
        sort_choice = get_valid_input(
            "\nОтсортировать операции по дате? (да/нет): ",
            lambda x: x.lower() in ["да", "нет"],
            "Пожалуйста, введите 'да' или 'нет'"
        ).lower()

        if sort_choice == "да":
            order = get_valid_input(
                "\nОтсортировать по возрастанию или убыванию? (возрастанию/убыванию): ",
                lambda x: x.lower() in ["возрастанию", "убыванию"],
                "Пожалуйста, введите 'возрастанию' или 'убыванию'"
            ).lower()

            reverse = order == "убыванию"
            transactions = sort_by_date(transactions, reverse)
            print(f"\nОперации отсортированы по {'убыванию' if reverse else 'возрастанию'} даты.")

        # 4. Фильтрация по валюте
        rub_choice = get_valid_input(
            "\nВыводить только рублевые транзакции? (да/нет): ",
            lambda x: x.lower() in ["да", "нет"],
            "Пожалуйста, введите 'да' или 'нет'"
        ).lower()

        if rub_choice == "да":
            rub_transactions = [
                t for t in transactions
                if 'currency_code' in t and t['currency_code'].lower() in ('rub', 'руб')
                   or 'currency_name' in t and re.search(r'rub|руб', t['currency_name'], re.IGNORECASE)
            ]
            print(f"\nНайдено {len(rub_transactions)} рублевых операций.")
            transactions = rub_transactions

        # 5. Поиск по описанию
        search_choice = get_valid_input(
            "\nОтфильтровать список транзакций по определенному слову в описании? (да/нет): ",
            lambda x: x.lower() in ["да", "нет"],
            "Пожалуйста, введите 'да' или 'нет'"
        ).lower()

        if search_choice == "да":
            search_word = input("Введите слово для поиска в описании: ").strip()
            if search_word:
                transactions = filter_transactions_by_description(transactions, search_word)
                print(f"\nНайдено {len(transactions)} операций с '{search_word}' в описании.")

        # 6. Вывод результатов
        print("\nРаспечатываю итоговый список транзакций...")
        print("=" * 50)

        if not transactions:
            print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
            for transaction in transactions:
                print(format_transaction(transaction))
                print("-" * 50)

        # 7. Дополнительная статистика
        stats_choice = get_valid_input(
            "\nПоказать статистику по категориям операций? (да/нет): ",
            lambda x: x.lower() in ["да", "нет"],
            "Пожалуйста, введите 'да' или 'нет'"
        ).lower()

        if stats_choice == "да" and transactions:
            default_categories = ["Перевод", "Покупка", "Оплата", "Вклад"]
            print(f"\nПримеры категорий: {', '.join(default_categories)}")
            categories = input("Введите категории через запятую: ").split(',')
            categories = [cat.strip() for cat in categories if cat.strip()]

            if categories:
                stats = count_transactions_by_category(transactions, categories)
                print("\nСтатистика по операциям:")
                for category, count in stats.items():
                    print(f"{category}: {count} операций")

    except Exception as e:
        print(f"\nПроизошла ошибка: {str(e)}")
        print("Пожалуйста, проверьте введенные данные и попробуйте снова.")


if __name__ == "__main__":
    main()
