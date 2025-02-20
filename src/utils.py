import json
import os
from config import DATA_DIR


def load_operation_json(data_file):
    file_path = os.path.join(DATA_DIR, data_file)
    if not os.path.exists(file_path):
        return []

    with open(file_path, encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []

print(load_operation_json('operations.json', currency 'usd'))
