import re
from collections import Counter
from typing import List, Dict


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Фильтрует транзакции по наличию строки в описании с использованием регулярных выражений.
    transactions: Список словарей с данными о транзакциях
    search_string: Строка для поиска в описании.
    """
    if not transactions or not search_string:
        return []

    try:
        pattern = re.compile(search_string, re.IGNORECASE)
    except re.error:
        return []

    return [t for t in transactions if "description" in t and pattern.search(t["description"])]


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций по категориям с использованием Counter.
    transactions: Список словарей с данными о транзакциях;
    categories: Список категорий для подсчета.
    """
    if not transactions or not categories:
        return {}

    # Собираем все описания, которые содержат хотя бы одну из категорий
    descriptions = []
    for t in transactions:
        if "description" in t:
            desc_lower = t["description"].lower()
            if any(cat.lower() in desc_lower for cat in categories):
                descriptions.append(t["description"])

    # Используем Counter для подсчета
    category_counter = Counter()

    for desc in descriptions:
        for category in categories:
            if re.search(r"\b" + re.escape(category.lower()) + r"\b", desc.lower()):
                category_counter[category] += 1

    return dict(category_counter)
