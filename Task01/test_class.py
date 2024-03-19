import pytest

from triangle_class import Triangle, IncorrectTriangleSides


def test_class_unit_establish():
    triangle = Triangle(10, 12, 14)

    assert triangle.get_a_side() == 10
    assert triangle.get_b_side() == 12
    assert triangle.get_c_side() == 14


def test_class_type_establish():
    triangle_nonequilateral = Triangle(10, 12, 14)
    triangle_equilateral = Triangle(10, 10, 10)
    triangle_isosceles = Triangle(10, 12, 10)

    assert triangle_nonequilateral.triangle_type() == 'nonequilateral'
    assert triangle_equilateral.triangle_type() == 'equilateral'
    assert triangle_isosceles.triangle_type() == 'isosceles'


def test_triangle_establish_negative_length_side():

    pytest.raises(IncorrectTriangleSides, Triangle, 10, -6, 10)

    with pytest.raises(IncorrectTriangleSides):
        Triangle(4, -4, 4)


def test_triangle_establish_zero_length_side():

    pytest.raises(IncorrectTriangleSides, Triangle, 10, 0, 10)


def test_triangle_establish_impossible_to_build_triangle():

    pytest.raises(IncorrectTriangleSides, Triangle, 18, 34, 14)


def test_triangle_establish_perimeter():

    assert Triangle(10, 12, 8).perimeter() == 30
    assert Triangle(10, 10, 10).perimeter() == 30


if __name__ == '__main__':
    test_class_unit_establish()
    test_class_type_establish()
    test_triangle_establish_negative_length_side()
    test_triangle_establish_zero_length_side()
    test_triangle_establish_impossible_to_build_triangle()
    test_triangle_establish_perimeter()
