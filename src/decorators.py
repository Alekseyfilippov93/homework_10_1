from functools import wraps


def log(filename=None):
    """Декоратор логирования функций, автоматически логирует начало и конец, и результаты и возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            function_name = func.__name__
            try:
                result = func(*args, **kwargs)
                log_message = f"{function_name} ok: {result}"
            except Exception as e:
                log_message = f"{function_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise  # пробрасываем исключение дальше
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
            return result

        return wrapper

    return decorator


# Пример использования декоратора
@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирует 2 числа"""
    return x + y

# Успешный вызов проверка
my_function(4, 5)


# Пример функции с ошибкой, где на ноль делить нельзя
@log(filename="mylog.txt")
def my_error_function(x, y):
    return x / y

my_error_function(1, 0)


