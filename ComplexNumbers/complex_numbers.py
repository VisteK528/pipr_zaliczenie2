from math import sqrt


class RealPartError(Exception):
    def __init__(self, real_part) -> None:
        super().__init__("Real part cannot be converted to float")
        self._real_part = real_part


class ImaginaryPartError(Exception):
    def __init__(self, imaginary_part) -> None:
        super().__init__("Imaginary part cannot be converted to float")
        self._imaginary_part = imaginary_part


class ComplexNumber:
    """
    Complex Number. Contains Attributes:
    :param real_part: real part of the complex number
    :type real_part: float
    :param imaginary_part: imaginary part of the complex number
    :type imaginary_part: float
    """
    def __init__(self, real_part, imaginary_part) -> None:
        if type(real_part) == str:
            if real_part.isdigit() is False:
                raise RealPartError(real_part)
            else:
                self._real_part = float(real_part)
        else:
            self._real_part = real_part

        if type(imaginary_part) == str:
            if imaginary_part.isdigit() is False:
                raise ImaginaryPartError(imaginary_part)
            else:
                self._imaginary_part = float(imaginary_part)
        else:
            self._imaginary_part = imaginary_part

    def get_real_part(self):
        """
        Returns real part
        """
        return self._real_part

    def set_real_part(self, real_part):
        """
        Sets real part if given value is a number.
        Otherwise raises RealPartError
        """
        if type(real_part) == str:
            if real_part.isdigit() is False:
                raise RealPartError(real_part)
            else:
                self._real_part = float(real_part)
        else:
            self._real_part = real_part

    def get_imaginary_part(self):
        """
        Retuns imaginary part
        """
        return self._imaginary_part

    def set_imaginary_part(self, imaginary_part):
        """
        Sets imaginary part if given value is a number.
        Otherwise raises ImaginaryPartError
        """
        if type(imaginary_part) == str:
            if imaginary_part.isdigit() is False:
                raise ImaginaryPartError(imaginary_part)
            else:
                self._imaginary_part = float(imaginary_part)
        else:
            self._imaginary_part = imaginary_part

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Adds two complex numbers and returns a complex number
        """
        real_part = self._real_part + other.get_real_part()
        imaginary_part = self._imaginary_part + other.get_imaginary_part()
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Subtracts two complex numbers and returns a complex number
        """
        real_part = self._real_part - other.get_real_part()
        imaginary_part = self._imaginary_part - other.get_imaginary_part()
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Multiplies two complex numbers and returns a complex number
        """
        a = self._real_part
        b = self._imaginary_part
        c = other.get_real_part()
        d = other.get_imaginary_part()

        real_part_result = a*c-b*d
        imaginary_part_result = a*d+b*c
        return ComplexNumber(real_part_result, imaginary_part_result)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Divides two complex numbers and returns a complex number
        """
        if not other.get_real_part() and not other.get_imaginary_part():
            raise ZeroDivisionError
        nominator = self.__mul__(other.conjugate())
        nominator_real = nominator.get_real_part()
        nominator_imaginary = nominator.get_imaginary_part()
        denominator = other*other.conjugate()
        denominator_real = denominator.get_real_part()
        nominator.set_real_part(nominator_real/denominator_real)
        nominator.set_imaginary_part(nominator_imaginary/denominator_real)
        return nominator

    def conjugate(self) -> "ComplexNumber":
        """
        Calculates conjugate of a complex number and returns it
        as new complex number
        """
        return ComplexNumber(self._real_part, -self._imaginary_part)

    def module(self) -> float:
        """
        Calculate module of the complex number and returns it as a float
        approximated to two decimal places
        """
        return round(sqrt(self._real_part**2+self._imaginary_part**2), 2)

    def __str__(self) -> str:
        """
        Returns visual representation of a complex number
        """
        imaginary_part_sign = '+' if self._imaginary_part >= 0 else "-"
        imaginary_part = abs(self._imaginary_part)
        if imaginary_part == 0:
            string = f"{self._real_part}"
        elif imaginary_part == 1:
            string = f"{self._real_part}{imaginary_part_sign}i"
        else:
            string = f"{self._real_part}{imaginary_part_sign}{imaginary_part}i"
        return string
