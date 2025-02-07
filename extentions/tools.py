from math import factorial as ft, e
from hashlib import sha256


def subfactorial(value: int):
    return str(round(ft(int(value)) / e))


def double_factorial(value: int):

    value = int(value)
    result = 1
    pre_result = []
    value_if_even = True if value % 2 == 0 else False
    for i in range(1, value + 1):
        if i % 2 == 0 and value_if_even:
            pre_result.append(i)
        elif i % 2 == 1 and not value_if_even:
            pre_result.append(i)
    for item in pre_result:
        result = result * item
    return str(result)


def tetration(count: int, value: int):
    result = int(value)
    for i in range(int(count) - 1):
        result = value ** result
    return result if not result.is_integer() else int(result)


def hash_encoder(text: str):
    return sha256(text.encode()).hexdigest()
