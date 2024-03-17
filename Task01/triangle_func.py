import doctest


class IncorrectTriangleSides(Exception):
    """

    Класс IncorrectTriangleSides выполняет роль custom-исключения.
    Вызывается в случае если одна или более сторон треугольника обладают отрицательными или нулевыми длинами.

    """
    def __init__(self, message="Длина одной или более сторон меньше либо равно нулю"):
        super().__init__(message)


def get_triangle_type(a_side: [int, float], b_side: [int, float], c_side: [int, float]) \
        -> [str, IncorrectTriangleSides]:
    """
    a_side, b_side, c_side - длины сторон треугольника;

    Функция возвращает строковое значение, описывающее тип треугольника

    :param a_side: int
    :param b_side: int
    :param c_side: int
    :return: str


    >>> get_triangle_type(4, 4, 4)
    'equilateral'

    >>> get_triangle_type(4, 7, 4)
    'isosceles'

    >>> get_triangle_type(4, 11, 8)
    'nonequilateral'

    >>> get_triangle_type(4, -4, 4)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Длина одной или более сторон меньше либо равно нулю

    >>> get_triangle_type(28, 10, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Длина одной из сторон превышает сумму длин двух других сторон


    """

    if type(a_side) not in [int, float] or \
            type(b_side) not in [int, float] or \
            type(c_side) not in [int, float]:

        raise IncorrectTriangleSides('Длины сторон не являются числовыми значениями')

    if a_side <= 0 or b_side <= 0 or c_side <= 0:
        raise IncorrectTriangleSides()

    if a_side + b_side < c_side or a_side + c_side < b_side or b_side + c_side < a_side:
        raise IncorrectTriangleSides('Длина одной из сторон превышает сумму длин двух других сторон')

    if a_side == b_side == c_side:
        return 'equilateral'
    elif a_side == b_side or b_side == c_side or a_side == c_side:
        return 'isosceles'
    else:
        return 'nonequilateral'


if __name__ == '__main__':

    print('\nДанные Check.txt\n')

    # Тест 1 - Равностороний треугольник

    print('Тест 1 - Равностороний треугольник:\n')

    a, b, c = 10, 10, 10

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-'*60, '\n')

    # Тест 2 - Равнобедренный треугольник

    print('Тест 2 - Равнобедренный треугольник:\n')

    a, b, c = 5, 10, 5

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-' * 60, '\n')

    # Тест 3 - Неравнобедренный треугольник

    print('Тест 3 - Неравнобедренный треугольник:\n')

    a, b, c = 7, 8, 9

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-' * 60, '\n')

    # Тест с помощью doctest

    # Успешный запуск, без ошибок
    
    doctest.testmod()

    # Тест 4 - Слишком длиная сторона

    print('Тест 4 - Слишком длиная сторона:\n')

    try:
        a, b, c = 28, 10, 5

        print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    except IncorrectTriangleSides as intrsi:

        print(f'Треугольник со сторонами a={a}, b={b}, c={c}: -> IncorrectTriangleSides: ' + str(intrsi), end='\n\n')

    print('-' * 140, '\n')

    # Тест 5 - Вывод ошибки при неправильном вводе длины

    print('Тест 5 - Вывод ошибки при неправильном вводе длины:\n')

    try:

        a, b, c = -4, 10, 5

        print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    except IncorrectTriangleSides as intrsi:

        print(f'Треугольник со сторонами a={a}, b={b}, c={c}: -> IncorrectTriangleSides: ' + str(intrsi), end='\n\n')

    print('-' * 140, '\n')

    # Тест 6 - Вывод ошибки при неправильном вводе длины

    print('Тест 6 - Вывод ошибки при неправильном вводе длины:\n')

    try:

        a, b, c = None, 10, 10

        print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    except IncorrectTriangleSides as intrsi:

        print(f'Треугольник со сторонами a={a}, b={b}, c={c}: -> IncorrectTriangleSides: ' + str(intrsi), end='\n\n')

    print('-' * 140, '\n')

    # Тест 7 - Ввод длины в формате float

    print('Тест 7 - Ввод длины в формате float:\n')

    a, b, c = 7.5, 8.2, 9.8

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-' * 60, '\n')

    # Тест 8 - Равнобедренный треугольник

    print('Тест 8 - Равнобедренный треугольник (float):\n')

    a, b, c = 10.5, 8.4, 10.5

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-' * 60, '\n')

    # Тест 9 - Равносторонний треугольник (float)

    print('Тест 9 - Равносторонний треугольник (float):\n')

    a, b, c = 11.8, 11.8, 11.8

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-' * 60, '\n')

    # Тест 10 - Неравнобедренный треугольник (float):

    print('Тест 10 - Неравнобедренный треугольник (float):\n')

    a, b, c = 4.8, 7.2, 7.7

    print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')

    print('-' * 60, '\n')

    # Вывод ошибки IncorrectTriangleSides в консоль

    # Traceback (most recent call last):
    #   File "D:\Documents\Python_files\Testing_Veshkin_LB1\triangle_func.py", line 49, in <module>
    #     print(f'Треугольник со сторонами a={a}, b={b}, c={c}:', get_triangle_type(a, b, c), end='\n\n')
    #                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   File "D:\Documents\Python_files\Testing_Veshkin_LB1\triangle_func.py", line 15, in get_triangle_type
    #     raise IncorrectTriangleSides()
    # IncorrectTriangleSides: Длина одной или более сторон меньше либо равно нулю


