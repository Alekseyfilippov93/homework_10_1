import pytest
from src.decorators import log


# Создаем функции с применением нашего декоратора. Потом уже тестируем
@log()
def add(x: int, y: int) -> int:
    return x + y


@log()
def divide(x: float, y: float) -> float:
    return x / y


# Првоерка сложения с использование декоратора
def test_add_success(capsys):
    add(2, 3)
    captured = capsys.readouterr()
    assert "add ok: 5" in captured.out


# Проверяем как функция отработает деление.
def test_divide_success(capsys):
    divide(10, 2)
    captured = capsys.readouterr()
    assert "divide ok: 5.0" in captured.out


# Проверка исключений, делить на ноль нельзя. Выдаст ошибку
def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


# Проверка с отрицательными числами
def test_add_negative(capsys):
    add(-1, -1)
    captured = capsys.readouterr()
    assert "add ok: -2" in captured.out
