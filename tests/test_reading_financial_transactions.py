import unittest
from unittest.mock import patch, Mock
from src.reading_financial_transactions import read_csv
from src.reading_financial_transactions import read_excel


class TestFinancialTransactions(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_csv(self, mock_read_csv):
        """Тестирование функции read_csv с использованием Mock."""
        # Создаем мок данных
        mock_data = [
            {'id': '1', 'amount': '100', 'description': 'Перевод организации'},
            {'id': '2', 'amount': '200', 'description': 'Перевод с карты на карту'}
        ]
        mock_df = Mock()
        mock_df.to_dict.return_value = mock_data
        mock_read_csv.return_value = mock_df

    @patch('pandas.read_excel')
    def test_read_excel(self, mock_read_excel):
        """Тестирование функции read_excel с использованием Mock."""
        # Создаем мок данных
        mock_data = [
            {'id': '1', 'amount': '100', 'description': 'Перевод организации'},
            {'id': '2', 'amount': '200', 'description': 'Перевод с карты на карту'}
        ]
        mock_df = Mock()
        mock_df.to_dict.return_value = mock_data
        mock_read_excel.return_value = mock_df
