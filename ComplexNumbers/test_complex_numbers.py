from complex_numbers import ComplexNumber, ImaginaryPartError, RealPartError
from pytest import raises


def test_create_complex_number():
    ComplexNumber(5, 1)


def test_create_complex_number_with_string_convertable():
    number = ComplexNumber("5", 1)
    assert number.get_real_part() == 5
    assert number.get_imaginary_part() == 1


def test_create_complex_number_with_string():
    with raises(RealPartError):
        ComplexNumber("w", 1)


def test_create_complex_number_with_string_2():
    with raises(ImaginaryPartError):
        ComplexNumber(1, "w")


def test_get_real_part():
    number1 = ComplexNumber(5, 1)
    assert number1.get_real_part() == 5


def test_get_imaginary_part():
    number1 = ComplexNumber(5, 1)
    assert number1.get_imaginary_part() == 1


def test_add_complex_numbers():
    number1 = ComplexNumber(5, 1)
    number2 = ComplexNumber(2, 6)
    number3 = number1 + number2
    assert number3.get_real_part() == 7
    assert number3.get_imaginary_part() == 7


def test_add_0_to_complex_number():
    number1 = ComplexNumber(5, 1)
    number2 = ComplexNumber(0, 0)
    number3 = number1 + number2
    assert number3.get_real_part() == 5
    assert number3.get_imaginary_part() == 1


def test_add_negative_complex_number():
    number1 = ComplexNumber(5, 1)
    number2 = ComplexNumber(-5, -1)
    number3 = number1 + number2
    assert number3.get_real_part() == 0
    assert number3.get_imaginary_part() == 0
    assert str(number3) == "0"


def test_subtract_two_complex_numbers():
    number1 = ComplexNumber(5, 1)
    number2 = ComplexNumber(2, 6)
    number3 = number1 - number2
    assert number3.get_real_part() == 3
    assert number3.get_imaginary_part() == -5


def test_multiply_complex_numbers():
    number1 = ComplexNumber(5, 1)
    number2 = ComplexNumber(2, 0)
    number3 = number1*number2
    assert number3.get_real_part() == 10
    assert number3.get_imaginary_part() == 2


def test_multiply_complex_numbers_2():
    number1 = ComplexNumber(5, 3)
    number2 = ComplexNumber(2, 7)
    number3 = number1*number2
    assert number3.get_real_part() == -11
    assert number3.get_imaginary_part() == 41


def test_div_complex_numbers():
    number1 = ComplexNumber(1, 8)
    number2 = ComplexNumber(2, 3)
    number3 = number1/number2
    assert number3.get_real_part() == 2
    assert number3.get_imaginary_part() == 1


def test_div_complex_numbers_by_0():
    number1 = ComplexNumber(1, 8)
    number2 = ComplexNumber(0, 0)
    with raises(ZeroDivisionError):
        number1/number2


def test_complex_number_conjugate():
    number1 = ComplexNumber(2, 3)
    number1_conjugate = number1.conjugate()
    assert number1_conjugate.get_real_part() == 2
    assert number1_conjugate.get_imaginary_part() == -3


def test_complex_number_module():
    number1 = ComplexNumber(2, 3)
    assert number1.module() == 3.61


def test_complex_number_string():
    number1 = ComplexNumber(1, 8)
    assert str(number1) == "1+8i"


def test_complex_number_string_negative():
    number1 = ComplexNumber(-1, -8)
    assert str(number1) == "-1-8i"


def test_complex_number_imaginary_part_0():
    number1 = ComplexNumber(-1, 0)
    assert str(number1) == "-1"


def test_complex_number_imaginary_part_1():
    number1 = ComplexNumber(-1, 1)
    assert str(number1) == "-1+i"
