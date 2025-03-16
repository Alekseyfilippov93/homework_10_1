import unittest
from unittest.mock import patch, Mock
import pandas as pd
from src.reading_financial_transactions import read_csv
from src.reading_financial_transactions import read_excel


class TestFinancialTransactions(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_csv(self, mock_read_csv):
        """Тестирование функции read_csv с использованием Mock."""
        # Создаем мок данных
        mock_data = [
            {'id': '650703', 'amount': '29740', 'description': 'Перевод организации'},
            {'id': '5380041', 'amount': '23789', 'description': 'Открытие вклада'}
        ]
        mock_df = Mock()
        mock_df.to_dict.return_value = mock_data
        mock_read_csv.return_value = mock_df

        # Вызываем тестируемую функцию
        result = read_csv('dummy_path.csv')

        # Проверяем, что функция возвращает ожидаемые данные
        self.assertEqual(result, mock_data)
        mock_read_csv.assert_called_once_with('dummy_path.csv')
        mock_df.to_dict.assert_called_once_with('records')

    @patch('pandas.read_excel')
    def test_read_excel(self, mock_read_excel):
        """Тестирование функции read_excel с использованием Mock."""
        # Создаем мок данных
        mock_data = [
            {'id': '650703', 'amount': '16210', 'description': 'Перевод организации'},
            {'id': '593027', 'amount': '30368', 'description': 'Перевод с карты на карту'}
        ]
        mock_df = Mock()
        mock_df.to_dict.return_value = mock_data
        mock_read_excel.return_value = mock_df

        # Вызываем тестируемую функцию
        result = read_excel('dummy_path.xlsx')

        # Проверяем, что функция возвращает ожидаемые данные
        self.assertEqual(result, mock_data)
        mock_read_excel.assert_called_once_with('dummy_path.xlsx')
        mock_df.to_dict.assert_called_once_with('records')

    @patch('pandas.read_excel')
    def test_read_excel_file_not_found(self, mock_read_excel):
        """Тестирование функции read_excel при отсутствии файла."""
        # Мокируем выброс исключения FileNotFoundError
        mock_read_excel.side_effect = FileNotFoundError("File not found")

        # Проверяем, что функция выбрасывает исключение
        with self.assertRaises(FileNotFoundError):
            read_excel('non_existent_path.xlsx')


@patch('pandas.read_csv')


def test_read_csv_invalid_file(self, mock_read_csv):
    """Тестирование функции read_csv при неверном формате файла."""
    # Мокируем выброс исключения pd.errors.EmptyDataError
    mock_read_csv.side_effect = pd.errors.EmptyDataError("No columns to parse from file")

    # Проверяем, что функция выбрасывает исключение
    with self.assertRaises(pd.errors.EmptyDataError):
        read_csv('invalid_file.csv')


@patch('pandas.read_excel')
def test_read_excel_invalid_file(self, mock_read_excel):
    """Тестирование функции read_excel при неверном формате файла."""
    # Мокируем выброс исключения pd.errors.EmptyDataError
    mock_read_excel.side_effect = pd.errors.EmptyDataError("No columns to parse from file")

    # Проверяем, что функция выбрасывает исключение
    with self.assertRaises(pd.errors.EmptyDataError):
        read_excel('invalid_file.xlsx')
