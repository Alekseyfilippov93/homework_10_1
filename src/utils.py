import json
import os
from config import DATA_DIR
from typing import List, Dict, Any


def load_operation_json(data_file: str) -> List[Dict[str, Any]]:
    """
    Загружает данные из JSON-файла.
    """
    file_path = os.path.join(DATA_DIR, data_file)

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        return []

    # Открываем и читаем файл
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, что данные являются списком
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, OSError):
        # Обрабатываем ошибки декодирования JSON и ошибки файловой системы
        return []

# transactions = load_operation_json("operations.json")
#
# # Выводим результат
# print(transactions)