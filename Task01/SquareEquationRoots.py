import math


class SquareEquation:
    """
    Класс SquareEquation разработан с целью решения квадратных уравнений

    Класс принимает на вход 3 коэффициента квадратного уравнения: a_cof, b_cof, c_cof

    Класс содержит 2 функции:

        1. extract_discriminant - функция, вычисляющая дискрименант уравнения. Принимает на вход коэффициенты a, b, c.
            В случае если коэффициенты не были переданны в функцию используются коэффициенты класса
            Возвращяет числовое значение дискременанта -> int;

        2. find_roots - функция, вычисляющая корни уравнения. Придусмотрена различна обработкакомблинаций коэффициентов.
            Возвращяет словарь состоящий из корней -> dict;

    """

    # Конструктор инициализации

    def __init__(self, a_cof, b_cof, c_cof):
        self.a = a_cof
        self.b = b_cof
        self.c = c_cof

        self.root_positive = None
        self.root_negative = None

    # Вычисление дискрименанта

    def extract_discriminant(self, a: int = None, b: int= None, c: int = None) -> int:
        """

        Функция вычисляет дискрименант квадратного уравнения, где a,b,c - коэффициенты

        :param a: int
        :param b: int
        :param c: int
        :return: int
        """
        if a is None or b is None or c is None:
            try:
                return math.sqrt(math.pow(self.b, 2) - 4*self.a*self.c)
            except ValueError:
                return -1

        return math.sqrt(math.pow(b, 2) - 4 * a * c)

    # Поиск корней

    def find_roots(self) -> dict:

        """

        Функция вычисления корней квадратного уравнения

        :return: dict -> {x1: x1_value, x2: x2_value}

        """

        if self.a == 0:
            try:

                return {'x': - self.c / self.b}

            except ZeroDivisionError as zero_div:

                return {'x': 0}

        local_discriminant = self.extract_discriminant()

        # Проверка на комплексные числа

        if local_discriminant < 0:

            return 'Полученны комплексные корни'

        self.root_positive = (-self.b + local_discriminant)/(2*self.a)

        self.root_negative = (-self.b - local_discriminant)/(2*self.a)

        # В случае одного корня выводит только его

        if self.root_negative == self.root_positive:

            return {'x': self.root_positive}

        return {'x1': self.root_positive, 'x2': self.root_negative}


if __name__ == '__main__':

    # Тест 1

    a, b, c = 5, -10, -15

    # Формируем вывод

    # \u00B2 - число, записанное в виде степени

    equation_text = f'{a}x\u00B2 + {b}x + {c} = 0' if b >= 0 else f'{a}x\u00B2 - {abs(b)}x + {c} = 0'

    print(f'Квадратное уравнение: {equation_text}\n')

    equation = SquareEquation(a_cof=a, b_cof=b, c_cof=c)

    print('Найденные корни:', equation.find_roots())

    print('-'*60, end='\n\n')

    # Тест 2

    a, b, c = 1, -4, 4

    # Формируем вывод

    # \u00B2 - число, записанное в виде степени

    equation_text = f'{a}x\u00B2 + {b}x + {c} = 0' if b >= 0 else f'{a}x\u00B2 - {abs(b)}x + {c} = 0'

    print(f'Квадратное уравнение: {equation_text}\n')

    equation = SquareEquation(a_cof=a, b_cof=b, c_cof=c)

    print('Найденные корни:', equation.find_roots())

    print('-'*60, end='\n\n')

    # Тест 3

    a, b, c = -5, -10, -15

    # Формируем вывод

    # \u00B2 - число, записанное в виде степени

    equation_text = f'{a}x\u00B2 + {b}x + {c} = 0' if b >= 0 else f'{a}x\u00B2 - {abs(b)}x + {c} = 0'

    print(f'Квадратное уравнение: {equation_text}\n')

    equation = SquareEquation(a_cof=a, b_cof=b, c_cof=c)

    print('Найденные корни:', equation.find_roots())

    print('-'*60, end='\n\n')

    # Тест 4

    a, b, c = 0, 4, -4

    # Формируем вывод

    # \u00B2 - число, записанное в виде степени

    equation_text = f'{a}x\u00B2 + {b}x + {c} = 0' if b >= 0 else f'{a}x\u00B2 - {abs(b)}x + {c} = 0'

    print(f'Квадратное уравнение: {equation_text}\n')

    equation = SquareEquation(a_cof=a, b_cof=b, c_cof=c)

    print('Найденные корни:', equation.find_roots())

    print('-'*60, end='\n\n')

    # Тест 5

    a, b, c = 0, 0, 0

    # Формируем вывод

    # \u00B2 - число, записанное в виде степени

    equation_text = f'{a}x\u00B2 + {b}x + {c} = 0' if b >= 0 else f'{a}x\u00B2 - {abs(b)}x + {c} = 0'

    print(f'Квадратное уравнение: {equation_text}\n')

    equation = SquareEquation(a_cof=a, b_cof=b, c_cof=c)

    print('Найденные корни:', equation.find_roots())

    print('-'*60, end='\n\n')

    # Тест 6

    a, b, c = 4, 4, 0

    # Формируем вывод

    # \u00B2 - число, записанное в виде степени

    equation_text = f'{a}x\u00B2 + {b}x + {c} = 0' if b >= 0 else f'{a}x\u00B2 - {abs(b)}x + {c} = 0'

    print(f'Квадратное уравнение: {equation_text}\n')

    equation = SquareEquation(a_cof=a, b_cof=b, c_cof=c)

    print('Найденные корни:', equation.find_roots())

    print('-' * 60, end='\n\n')

