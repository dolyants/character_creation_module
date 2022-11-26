from math import sqrt

"""Вычисление квадратного кореня из заданного числа."""
message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Расчет квадратного корня."""
    calc_number = calculate_square_root(your_number)
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {calc_number}')


print(message)
calc(25.5)