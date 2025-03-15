from typing import List, Dict
import pandas as pd


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """Читает операции из CSV-файла и возвращает список словарей."""
    df = pd.read_csv(file_path)
    return df.to_dict('records')


def read_excel(file_path: str) -> List[Dict[str, str]]:
    """Читает финансовые операции из Excel-файла и возвращает список словарей."""
    df = pd.read_excel(file_path)
    return df.to_dict('records')
