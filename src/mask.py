import logging
import os
from typing import Union

# Определяем корневую папку проекта
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Переход на уровень выше src
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')  # Путь к папке logs в корне проекта

# Создаем папку logs, если она не существует
if not os.path.exists(LOGS_DIR):
    print(f"Создаем папку logs в {LOGS_DIR}...")
    os.makedirs(LOGS_DIR)

# Настройка логера для модуля masks
masks_logger = logging.getLogger('masks')
masks_logger.setLevel(logging.DEBUG)  # Уровень логирования не меньше DEBUG

# Настройка FileHandler для модуля masks
log_file_path = os.path.join(LOGS_DIR, 'masks.log')  # Путь к файлу логов
masks_file_handler = logging.FileHandler(log_file_path, mode='w')
masks_file_handler.setLevel(logging.DEBUG)

# Настройка форматера для модуля masks
masks_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
masks_file_handler.setFormatter(masks_formatter)

# Добавляем handler к логеру модуля masks
masks_logger.addHandler(masks_file_handler)

# Отладочное сообщение
print(f"Логер для модуля masks настроен. Логи будут записаны в {log_file_path}")


# Функция, принимающая номер карты, и возвращающая ее маску
def get_mask_card_number(numbers: Union[str]) -> Union[str]:
    """
    Принимает на вход номер карты в виде строки и возвращает маску номера по правилу XXXX XX** **** XXXX.
    """
    masks_logger.debug(f"Начало выполнения функции get_mask_card_number с номером: {numbers}")

    if len(numbers) != 16:
        error_msg = "Неверный ввод карты. Номер карты состоит из 16 чисел"
        masks_logger.error(error_msg)
        raise ValueError(error_msg)

    masked_number = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[12:]}"
    masks_logger.debug(f"Маскированный номер карты: {masked_number}")
    return masked_number


# Функция маскировки номера банковского счета
def get_mask_account(mask_account: Union[str]) -> Union[str]:
    """
    Принимает на вход номер счета в виде строки и возвращает маску номера по правилу **XXXX.
    """
    masks_logger.debug(f"Начало выполнения функции get_mask_account с номером: {mask_account}")

    if len(mask_account) < 4:
        error_msg = "Неверный ввод счета. Номер счета должен содержать не менее 4 символов"
        masks_logger.error(error_msg)
        raise ValueError(error_msg)

    masked_account = "**" + mask_account[-4:]
    masks_logger.debug(f"Маскированный номер счета: {masked_account}")
    return masked_account


if __name__ == "__main__":
    # Пример использования функций
    try:
        print(get_mask_card_number("6468647367889477"))
        print(get_mask_account("64686473678894779589"))
    except ValueError as e:
        masks_logger.error(f"Ошибка в main: {e}")