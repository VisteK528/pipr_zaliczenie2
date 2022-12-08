
class CityRentPriceError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Office:
    def __init__(self, city, area, rooms, unit_number) -> None:
        self._city = city
        if area < 0:
            raise ValueError("Area value cannot be negative")
        self._area = area
        if rooms < 0:
            raise ValueError("Rooms number cannot be negative")
        self._rooms = rooms
        if unit_number < 0:
            raise ValueError("Unit number cannot be negative")
        self._unit_number = unit_number

    def get_city(self):
        return self._city

    def set_city(self, city):
        self._city = city

    def get_area(self):
        return self._area

    def set_area(self, area):
        if area < 0:
            raise ValueError("Area value cannot be negative")
        self._area = area

    def get_rooms(self):
        return self._rooms

    def set_rooms(self, rooms):
        if rooms < 0:
            raise ValueError("Rooms number cannot be negative")
        self._rooms = rooms

    def get_unit_number(self):
        return self._unit_number

    def set_unit_number(self, unit_number):
        if unit_number < 0:
            raise ValueError("Unit number cannot be negative")
        self._unit_number = unit_number


def rent_cost(office, prices):
    if not office.get_city() in prices.keys():
        raise CityRentPriceError(
            "City name is not included in rent prices database")
    return office.get_area() * prices[office.get_city()]


def max_employees_in_office(office, employees_in_room, area_per_employee):
    max_employees_by_area = office.get_area()//area_per_employee
    max_employees_by_rooms = office.get_rooms()*employees_in_room
    return min(max_employees_by_area, max_employees_by_rooms)
