import json
import os
import logging
from typing import List, Dict, Any
from config import DATA_DIR

# Определяем корневую папку проекта
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Переход на уровень выше src
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')  # Путь к папке logs в корне проекта

# Создаем папку logs, если она не существует
if not os.path.exists(LOGS_DIR):
    print(f"Создаем папку logs в {LOGS_DIR}...")
    os.makedirs(LOGS_DIR)

# Настройка логера для модуля utils
utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)

# Настройка FileHandler для модуля utils
log_file_path = os.path.join(LOGS_DIR, 'utils.log')  # Путь к файлу логов
utils_file_handler = logging.FileHandler(log_file_path, mode='w')  # Перезаписывается каждый раз
utils_file_handler.setLevel(logging.DEBUG)

# Настройка форматера для модуля utils
utils_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
utils_file_handler.setFormatter(utils_formatter)

# Добавляем handler к логеру модуля utils
utils_logger.addHandler(utils_file_handler)


def load_operation_json(data_file: str) -> List[Dict[str, Any]]:
    """
    Загружает данные из JSON-файла.
    """
    file_path = os.path.join(DATA_DIR, data_file)

    # Логируем начало
    utils_logger.debug(f"Начало загрузки данных из файла: {file_path}")

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        utils_logger.error(f"Файл не найден: {file_path}")
        return []

    # Открываем и читаем файл
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, что данные являются списком
            if isinstance(data, list):
                utils_logger.debug(f"Данные успешно загружены из файла: {file_path}")
                return data
            else:
                utils_logger.error(f"Данные в файле {file_path} не являются списком")
                return []
    except json.JSONDecodeError as e:
        # Логируем ошибку
        utils_logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
    except OSError as e:
        # Логируем ошибку системы
        utils_logger.error(f"Ошибка файловой системы при работе с файлом {file_path}: {e}")
        return []
