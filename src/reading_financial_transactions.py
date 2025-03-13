from typing import List, Dict
import pandas as pd

def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Читает финансовые операции из CSV-файла и возвращает список словарей.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    file_path = 'transactions.csv'
    df = pd.read_csv('transactions')
    return df.to_dict('records')

def read_excel("transactions_excel") -> List[Dict[str, str]]:
    """
    Читает финансовые операции из Excel-файла и возвращает список словарей.

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    file_path = transactions_excel
    df = pd.read_excel('transactions_excel')
    return df.to_dict('records')