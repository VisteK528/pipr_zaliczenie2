from classes import (
    Program,
    Mask,
    NoSuppliesError,
    UnknownFabricError,
    UnknownFixingError,
    UnknownSizeError)
from pytest import raises


def test_generate_report():
    supplies = {
        "len": 20, "bawełna": 18, "jedwab": 15,
        "gumka": 35, "tasiemka": 50}
    units = {
        "len": "mb", "bawełna": "mb",
        "jedwab": "mb", "gumka": "m", "tasiemka": "m"}
    expected_report = "| Zasób    | Ilość w magazynie |\n"\
                      "| -------- | ----------------- |\n"\
                      "| len      |             20 mb |\n"\
                      "| bawełna  |             18 mb |\n"\
                      "| jedwab   |             15 mb |\n"\
                      "| gumka    |              35 m |\n"\
                      "| tasiemka |              50 m |\n"
    program = Program(supplies, units, [])
    assert program.generate_report() == expected_report


def test_complete_order():
    supplies = {
        "len": 20, "bawełna": 18, "jedwab": 15,
        "gumka": 35, "tasiemka": 50}
    units = {
        "len": "mb", "bawełna": "mb",
        "jedwab": "mb", "gumka": "m", "tasiemka": "m"}
    production_costs = {
        "materiał": {
            "bawełna": {"S/M": 0.25, "L": 0.27},
            "len": {"S": 0.44, "M": 0.5, "L": 0.54},
            "jedwab": {"U": 0.26}},
        "mocowanie": {"tasiemka": 1.2, "gumka": 0.3}}
    program = Program(supplies, units, production_costs)
    order_list = [Mask("bawełna", "S/M", "tasiemka"),
                  Mask("bawełna", "L", "gumka"),
                  Mask("jedwab", "U", "gumka"),
                  Mask("bawełna", "S/M", "tasiemka")]
    expected_costs = {"bawełna": 0.77, "jedwab": 0.26,
                      "gumka": 0.6, "tasiemka": 2.4}
    assert program.complete_order(order_list) == expected_costs


def test_complete_order_with_no_enough_supplies():
    supplies = {
        "len": 20, "bawełna": 18, "jedwab": 15,
        "gumka": 35, "tasiemka": 50}
    units = {
        "len": "mb", "bawełna": "mb",
        "jedwab": "mb", "gumka": "m", "tasiemka": "m"}
    production_costs = {
        "materiał": {
            "bawełna": {"S/M": 0.25, "L": 0.27},
            "len": {"S": 0.44, "M": 0.5, "L": 0.54},
            "jedwab": {"U": 0.26}},
        "mocowanie": {"tasiemka": 1.2, "gumka": 0.3}}
    program = Program(supplies, units, production_costs)
    order_list = [Mask("bawełna", "S/M", "tasiemka") for _ in range(100)]
    with raises(NoSuppliesError):
        program.complete_order(order_list)


def test_complete_order_with_unknown_fabric():
    supplies = {
        "len": 20, "bawełna": 18, "jedwab": 15,
        "gumka": 35, "tasiemka": 50}
    units = {
        "len": "mb", "bawełna": "mb",
        "jedwab": "mb", "gumka": "m", "tasiemka": "m"}
    production_costs = {
        "materiał": {
            "bawełna": {"S/M": 0.25, "L": 0.27},
            "len": {"S": 0.44, "M": 0.5, "L": 0.54},
            "jedwab": {"U": 0.26}},
        "mocowanie": {"tasiemka": 1.2, "gumka": 0.3}}
    program = Program(supplies, units, production_costs)
    order_list = [Mask("denim", "S/M", "tasiemka")]
    with raises(UnknownFabricError):
        program.complete_order(order_list)


def test_complete_order_with_unknown_size():
    supplies = {
        "len": 20, "bawełna": 18, "jedwab": 15,
        "gumka": 35, "tasiemka": 50}
    units = {
        "len": "mb", "bawełna": "mb",
        "jedwab": "mb", "gumka": "m", "tasiemka": "m"}
    production_costs = {
        "materiał": {
            "bawełna": {"S/M": 0.25, "L": 0.27},
            "len": {"S": 0.44, "M": 0.5, "L": 0.54},
            "jedwab": {"U": 0.26}},
        "mocowanie": {"tasiemka": 1.2, "gumka": 0.3}}
    program = Program(supplies, units, production_costs)
    order_list = [Mask("bawełna", "U", "tasiemka")]
    with raises(UnknownSizeError):
        program.complete_order(order_list)


def test_complete_order_with_unknown_fixing():
    supplies = {
        "len": 20, "bawełna": 18, "jedwab": 15,
        "gumka": 35, "tasiemka": 50}
    units = {
        "len": "mb", "bawełna": "mb",
        "jedwab": "mb", "gumka": "m", "tasiemka": "m"}
    production_costs = {
        "materiał": {
            "bawełna": {"S/M": 0.25, "L": 0.27},
            "len": {"S": 0.44, "M": 0.5, "L": 0.54},
            "jedwab": {"U": 0.26}},
        "mocowanie": {"tasiemka": 1.2, "gumka": 0.3}}
    program = Program(supplies, units, production_costs)
    order_list = [Mask("bawełna", "S/M", "sznurek")]
    with raises(UnknownFixingError):
        program.complete_order(order_list)


def test_get_fabric():
    mask = Mask("bawełna", "S/M", "sznurek")
    assert mask.get_fabric() == "bawełna"


def test_set_fabric():
    mask = Mask("bawełna", "S/M", "sznurek")
    assert mask.get_fabric() == "bawełna"
    mask.set_fabric("dżins")
    assert mask.get_fabric() == "dżins"


def test_get_size():
    mask = Mask("bawełna", "S/M", "sznurek")
    assert mask.get_size() == "S/M"


def test_set_size():
    mask = Mask("bawełna", "S/M", "sznurek")
    assert mask.get_size() == "S/M"
    mask.set_size("L")
    assert mask.get_size() == "L"


def test_get_fixing():
    mask = Mask("bawełna", "S/M", "sznurek")
    assert mask.get_fixing() == "sznurek"


def test_set_fixing():
    mask = Mask("bawełna", "S/M", "sznurek")
    assert mask.get_fixing() == "sznurek"
    mask.set_fixing("gumka")
    assert mask.get_fixing() == "gumka"
