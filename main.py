import math


def delta(a: int, b: int, c: int):
    return math.pow(b, 2) - 4 * a * c


def bhaskara(a: int, b: int, c: int):
    delta_value = delta(a, b, c)

    if delta_value < 0:
        return "Delta Negativo"

    delta_root = round(math.sqrt(delta_value), 2)

    x1 = round((-b + delta_root / 2 * a), 2)
    x2 = round((-b - delta_root / 2 * a), 2)
    return f"x1 = {x1}, x2 = {x2}"


print(bhaskara(7, 3, 4))
# Delta Negativo

print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56

print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12


def corresponding_parenthesis(text: str):
    opening = text.count("(")
    closing = text.count(")")
    difference = opening - closing

    if difference > 0:
        return "(" * difference
    elif difference < 0:
        return ")" * (difference * -1)

    return "''"


result = corresponding_parenthesis("()()")
print(result)
# ''

result_2 = corresponding_parenthesis("()))")
print(result_2)
# '))'

result_3 = corresponding_parenthesis(")))(((((")
print(result_3)
# '(('


def remove_more_than_two_repetitions(text: str):
    pass
