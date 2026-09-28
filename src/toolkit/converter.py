from .errors import (
    Below_Absolute_Zero_Error,
    Incompatible_Units_Error,
    Unknown_Unit_Error,
)

"""converter.py"""
table :dict[str, dict[str,float | None]]={
    "length": {
        "mm": 0.001,
        "cm": 0.01,
        "m":  1.0,
        "km": 1000.0,
    },
    "mass": {
        "g":  0.001,
        "kg": 1.0,
    },
    "temp": {
        "c": None,
        "f": None,
        "k": None,
    },
}
"""Find group of units"""
def find_group(unit:str)->str | None:
    for group, units in table.items():
        if unit in units:
            return group
    return None

"""Converting temperature to celcius"""
def to_celsius(value: float, unit: str)->float:
    if unit == "c":
        return value
    if unit == "f":
        return (value - 32) * 5 / 9
    return value - 273.15

"""Converting temperature from celcius"""
def from_celsius(value: float, unit: str)-> float:
    if unit == "c":
        return value
    if unit == "f":
        return value * 9 / 5 + 32
    return value + 273.15

"""Convert temperature"""
def convert_temp(value: float, from_unit: str, to_unit: str)->float:
    celsius = to_celsius(value, from_unit)
    if celsius < -273.15:
        raise Below_Absolute_Zero_Error("температура ниже абсолютного нуля")
    return from_celsius(celsius, to_unit)

"""Convert lenght and mass"""
def convert_ratio(value: float, from_unit: str, to_unit: str)-> float:
    group = find_group(from_unit)
    base = value * table[group][from_unit]
    return base / table[group][to_unit]

"""All convert"""
def convert(value: float, from_unit: str, to_unit: str)-> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    group_from = find_group(from_unit)
    group_to = find_group(to_unit)

    if group_from is None:
        raise Unknown_Unit_Error("неизвестная единица: " + from_unit)
    if group_to is None:
        raise Unknown_Unit_Error("неизвестная единица: " + to_unit)
    if group_from != group_to:
        raise Incompatible_Units_Error("несовместимые единицы: " + from_unit + " и " + to_unit)

    if group_from == "temp":
        return convert_temp(value, from_unit, to_unit)

    return convert_ratio(value, from_unit, to_unit)
