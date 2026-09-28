import pytest

from toolkit import (
    Below_Absolute_Zero_Error,
    Incompatible_Units_Error,
    Unknown_Unit_Error,
    convert,
)

"""Тесты ядра конвертера."""


"""Успешные"""

def test_km_to_m()->None:
    assert convert(5, "km", "m") == 5000.0


def test_m_to_km()->None:
    assert convert(5000, "m", "km") == 5.0


def test_kg_to_g()->None:
    assert convert(1, "kg", "g") == 1000.0


def test_uppercase_units()->None:
    assert convert(5, "KM", "M") == 5000.0


def test_c_to_f()->None:
    assert convert(100, "c", "f") == 212.0


def test_f_to_c()->None:
    assert convert(32, "f", "c") == 0.0


def test_c_to_k()->None:
    assert convert(0, "c", "k") == 273.15


def test_absolute_zero_ok()->None:
    assert convert(-273.15, "c", "k") == 0.0

"""Негативные"""

def test_unknown_from_unit()->None:
    with pytest.raises(Unknown_Unit_Error):
        convert(5, "xx", "m")


def test_unknown_to_unit()->None:
    with pytest.raises(Unknown_Unit_Error):
        convert(5, "m", "xx")


def test_incompatible_units()->None:
    with pytest.raises(Incompatible_Units_Error):
        convert(5, "km", "kg")


def test_below_absolute_zero()->None:
    with pytest.raises(Below_Absolute_Zero_Error):
        convert(-300, "c", "k")
