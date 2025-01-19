import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date


# Функции для проверки тестов
def test_filter_by_state(dict_1):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == dict_1
    )


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            [{"date": "2023-01-01"}, {"date": "2022-01-01"}, {"date": "2024-01-01"}],
            [{"date": "2024-01-01"}, {"date": "2023-01-01"}, {"date": "2022-01-01"}],
        ),
        # Тесты на одинаковые даты
        (
            [{"date": "2022-01-01", "name": "A"}, {"date": "2022-01-01", "name": "B"}],
            [{"date": "2022-01-01", "name": "A"}, {"date": "2022-01-01", "name": "B"}],
        ),
    ],
)
def test_sort_by_date(input_data, expected_output):
    assert sort_by_date(input_data) == expected_output
