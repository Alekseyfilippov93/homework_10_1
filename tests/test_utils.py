from unittest.mock import patch, mock_open
from src.utils import load_operation_json


def test_load_valid_json():
    """
    Тест на успешную загрузку JSON-файла.
    """
    with patch("os.path.exists", return_value=True), patch(
            "builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]'
    ):
        result = load_operation_json("operations.json")
        assert result == [{"id": 1, "amount": 100}]


def test_file_not_found():
    """
    Тест на случай, если файл не существует.
    """
    with patch("os.path.exists", return_value=False):
        result = load_operation_json("nonexistent.json")
        assert result == []
