from typing import Sequence


class NoSuppliesError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknownFabricError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknownSizeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknownFixingError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Mask:
    def __init__(self, fabric, size, fixing) -> None:
        self._fabric = fabric
        self._size = size
        self._fixing = fixing

    def get_fabric(self):
        return self._fabric

    def set_fabric(self, fabric):
        self._fabric = fabric

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size

    def get_fixing(self):
        return self._fixing

    def set_fixing(self, fixing):
        self._fixing = fixing


class Program:
    def __init__(self, supplies, units, production_costs) -> None:
        self._supplies = supplies
        self._units = units
        self._production_costs = production_costs

    def generate_report(self) -> str:
        """
        Generates report of current status of the storage
        and returns it as a string
        """
        width = 8
        width2 = 17
        header1 = "Zasób"
        header2 = "Ilość w magazynie"
        report = f"| {header1:<{width}} | {header2:<{width2}} |\n"
        report += f"| {'-'*width} | {'-'*width2} |\n"
        for name, amount in self._supplies.items():
            amount_formatted = f"{amount} {self._units[name]}"
            report += f"| {name:<{width}} | {amount_formatted:>{width2}} |\n"
        return report

    def _check_if_in_storage(self, fabric, size, fixing) -> None:
        """
        Checks if the mask fabric and mask fixing types are in the storage
        and if mask size is among available designs
        """
        if fabric not in self._production_costs["materiał"].keys():
            raise UnknownFabricError
        if size not in self._production_costs["materiał"][fabric].keys():
            raise UnknownSizeError
        if fixing not in self._production_costs["mocowanie"].keys():
            raise UnknownFixingError

    def _check_if_enough_supplies(self, used_supplies) -> bool:
        """
        Checks if there is enought supplies
        in the storage to complete the order
        """
        for supply, amount in used_supplies.items():
            if (self._supplies[supply] - amount) < 0:
                return False
        return True

    def complete_order(self, order: Sequence[Mask]) -> dict:
        """
        Calculates how much fabric of each type is needed to complete corder,
        and if there is enough fabric in the storage returns
        dict of used supplies
        """
        used_supplies = {}
        for mask in order:
            fabric = mask.get_fabric()
            size = mask.get_size()
            fixing = mask.get_fixing()
            self._check_if_in_storage(fabric, size, fixing)
            fabric_amount = used_supplies.get(fabric, 0)
            fabric_amount += self._production_costs["materiał"][fabric][size]
            used_supplies.update({fabric: fabric_amount})
            fixing_amount = used_supplies.get(fixing, 0)
            fixing_amount += self._production_costs["mocowanie"][fixing]
            used_supplies.update({fixing: fixing_amount})

        if not self._check_if_enough_supplies(used_supplies):
            message = "There isn't enough supplies in "\
                          "the storage to complete the order"
            raise NoSuppliesError(message)

        return used_supplies
