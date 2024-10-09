def division_remainder(dividend, divisor):
    """
    Возвращает остаток от деления dividend на divisor.
    Если divisor равен нулю, генерируется исключение ValueError.
    Если типы аргументов некорректны, генерируется исключение TypeError.
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Оба аргумента должны быть числами (int или float)")

    if divisor == 0:
        raise ValueError("Деление на ноль невозможно")

    return dividend % divisor
