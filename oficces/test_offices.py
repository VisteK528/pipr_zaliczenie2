from offices import (
    Office,
    rent_cost,
    max_employees_in_office,
    CityRentPriceError)
from pytest import raises


def test_create_office():
    data = [
        {"Miejscowosc": "Warszawa", "Powierzchnia": 700,
         "Liczba_pomieszczen": 10, "Nr_oddzialu": 1},
        {"Miejscowosc": "Kraków", "Powierzchnia": 380,
         "Liczba_pomieszczen": 5, "Nr_oddzialu": 2},
        {"Miejscowosc": "Poznań", "Powierzchnia": 650,
         "Liczba_pomieszczen": 11, "Nr_odzialu": 3},
        {"Miejscowosc": "Białystok", "Powierzchnia": 800,
         "Liczba_pomieszczen": 12, "Nr_oddziału": 4}]
    Office(*data[1].values())


def test_calculate_rent_cost():
    data = [
        {"Miejscowosc": "Warszawa", "Powierzchnia": 700,
         "Liczba_pomieszczen": 10, "Nr_oddzialu": 1},
        {"Miejscowosc": "Kraków", "Powierzchnia": 380,
         "Liczba_pomieszczen": 5, "Nr_oddzialu": 2},
        {"Miejscowosc": "Poznań", "Powierzchnia": 650,
         "Liczba_pomieszczen": 11, "Nr_odzialu": 3},
        {"Miejscowosc": "Białystok", "Powierzchnia": 800,
         "Liczba_pomieszczen": 12, "Nr_oddziału": 4}]

    cost_data = {"Warszawa": 100, "Kraków": 70, "Poznań": 45, "Białystok": 30}
    office = Office(*data[0].values())
    results = 70000
    assert rent_cost(office, cost_data) == results


def test_calculate_max_employees_in_office():
    data = [
        {"Miejscowosc": "Warszawa", "Powierzchnia": 700,
         "Liczba_pomieszczen": 10, "Nr_oddzialu": 1},
        {"Miejscowosc": "Kraków", "Powierzchnia": 380,
         "Liczba_pomieszczen": 5, "Nr_oddzialu": 2},
        {"Miejscowosc": "Poznań", "Powierzchnia": 650,
         "Liczba_pomieszczen": 11, "Nr_odzialu": 3},
        {"Miejscowosc": "Białystok", "Powierzchnia": 800,
         "Liczba_pomieszczen": 12, "Nr_oddziału": 4}]

    office = Office(*data[0].values())
    max_people_in_office = 20
    assert max_employees_in_office(office, 2, 15) == max_people_in_office


def test_calculate_rent_cost_with_unsupported_city():
    cost_data = {"Warszawa": 100, "Kraków": 70, "Poznań": 45, "Białystok": 30}
    office = Office("Kielce", 250, 5, 5)
    with raises(CityRentPriceError):
        rent_cost(office, cost_data)


def test_calculate_max_employees_in_all_cities():
    cities = [
        {"Miejscowosc": "Warszawa", "Powierzchnia": 700,
         "Liczba_pomieszczen": 10, "Nr_oddzialu": 1},
        {"Miejscowosc": "Kraków", "Powierzchnia": 380,
         "Liczba_pomieszczen": 5, "Nr_oddzialu": 2},
        {"Miejscowosc": "Poznań", "Powierzchnia": 650,
         "Liczba_pomieszczen": 11, "Nr_odzialu": 3},
        {"Miejscowosc": "Białystok", "Powierzchnia": 800,
         "Liczba_pomieszczen": 12, "Nr_oddziału": 4}]
    expected_results = [20, 10, 22, 24]

    for office_data, exptected_result in zip(cities, expected_results):
        office = Office(*office_data.values())
        assert max_employees_in_office(office, 2, 15) == exptected_result


def test_get_city():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_city() == "Kielce"


def test_set_city():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_city() == "Kielce"
    office.set_city("Lublin")
    assert office.get_city() == "Lublin"


def test_get_area():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_area() == 250


def test_set_area():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_area() == 250
    office.set_area(200)
    assert office.get_area() == 200


def test_get_rooms():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_rooms() == 5


def test_set_rooms():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_rooms() == 5
    office.set_rooms(7)
    assert office.get_rooms() == 7


def test_set_rooms_negative():
    office = Office("Kielce", 250, 5, 5)
    assert office.get_rooms() == 5
    with raises(ValueError):
        office.set_rooms(-5)
