class IncorrectTriangleSides(Exception):
    """

        Класс IncorrectTriangleSides выполняет роль custom-исключения.
        Вызывается в случае если одна или более сторон треугольника обладают отрицательными или нулевыми длинами.

        """

    def __init__(self, message="Длина одной или более сторон меньше либо равно нулю"):
        super().__init__(message)


class Triangle(object):

    def __init__(self, a_side, b_side, c_side):

        if type(a_side) not in [int, float] or \
                type(b_side) not in [int, float] or \
                type(c_side) not in [int, float]:
            raise IncorrectTriangleSides('Длины сторон не являются числовыми значениями')

        if a_side <= 0 or b_side <= 0 or c_side <= 0:
            raise IncorrectTriangleSides()

        if a_side + b_side < c_side or a_side + c_side < b_side or b_side + c_side < a_side:
            raise IncorrectTriangleSides('Длина одной из сторон превышает сумму длин двух других сторон')

        # Компоненты класса имеют закрытый тип (private)

        self.__a_side = a_side
        self.__b_side = b_side
        self.__c_side = c_side

    # Функция для предоставления доступа к закрытому атрибуту класса (Сторона А)

    def get_a_side(self):
        return self.__a_side

    # Функция для предоставления доступа к закрытому атрибуту класса (Сторона B)

    def get_b_side(self):
        return self.__b_side

    # Функция для предоставления доступа к закрытому атрибуту класса (Сторона C)

    def get_c_side(self):
        return self.__c_side

    def triangle_type(self):

        if self.__a_side == self.__b_side == self.__c_side:
            return 'equilateral'
        elif self.__a_side == self.__b_side or self.__b_side == self.__c_side or self.__a_side == self.__c_side:
            return 'isosceles'
        else:
            return 'nonequilateral'

    def perimeter(self):

        return self.__a_side + self.__b_side + self.__c_side
