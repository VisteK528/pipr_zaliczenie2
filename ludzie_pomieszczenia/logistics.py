

class Program:
    def __init__(self, max_employees, area_per_employee, data) -> None:
        self._max_employees = max_employees
        self._area_per_employee = area_per_employee
        self._data = data

    def max_employees_in_office(self):
        results = []
        for office in self._data:
            results.append(
                min(office["Powierzchnia"]//self._area_per_employee,
                    office["Liczba_pomieszczen"]*self._max_employees))
        return self._generate_results(results)

    def calculate_rent_costs(self, cost_data):
        results = []
        for office in self._data:
            price = cost_data[office["Miejscowosc"]]
            results.append(price*office["Powierzchnia"])
        return self._generate_results(results)

    def _generate_results(self, data):
        cities = [city["Miejscowosc"] for city in self._data]
        return {city: data for city, data in zip(cities, data)}


if __name__ == "__main__":
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

    program = Program(2, 15, data)
    print(program.max_employees_in_office())
    print(program.calculate_rent_costs(cost_data))
