"""Тесты вычислительного ядра калькулятора."""

import pytest

from toolkit import (
    Division_By_Zero_Error,
    Empty_Expression_Error,
    Invalid_Number_Error,
    Missing_Operand_Error,
    Unknown_Symbol_Error,
    calculate,
    tokenisation,
    validation,
)

"""Успешные"""
def test_simple_sum()->None:
    tokens = tokenisation("2+2")
    validation(tokens)
    assert calculate(tokens) == 4.0


def test_priority_mul_over_plus()->None:
    tokens = tokenisation("2+2*2")
    validation(tokens)
    assert calculate(tokens) == 6.0


def test_priority_div_over_minus()->None:
    tokens = tokenisation("10-4/2")
    validation(tokens)
    assert calculate(tokens) == 8.0


def test_unary_minus()->None:
    tokens = tokenisation("-2+3")
    validation(tokens)
    assert calculate(tokens) == 1.0


def test_unary_plus()->None:
    tokens = tokenisation("+2+3")
    validation(tokens)
    assert calculate(tokens) == 5.0


def test_spaces_ignored()->None:
    tokens = tokenisation("  2  +  2  ")
    validation(tokens)
    assert calculate(tokens) == 4.0


def test_float_numbers()->None:
    tokens = tokenisation("1.5+2.25")
    validation(tokens)
    assert calculate(tokens) == 3.75


def test_int_division()->None:
    tokens = tokenisation("10//3")
    validation(tokens)
    assert calculate(tokens) == 3.0


def test_modulo()->None:
    tokens = tokenisation("10%3")
    validation(tokens)
    assert calculate(tokens) == 1.0

def test_unary_minus_both_operands()->None:
    tokens = tokenisation("-2 * -3")
    validation(tokens)
    assert calculate(tokens) == 6.0


def test_plus_then_unary_minus()->None:
    tokens = tokenisation("1+-2")
    validation(tokens)
    assert calculate(tokens) == -1.0


"""Негативные"""

def test_empty_expression()->None:
    with pytest.raises(Empty_Expression_Error):
        tokenisation("   ")


def test_unknown_symbol()->None:
    with pytest.raises(Unknown_Symbol_Error):
        tokenisation("2 & 3")


def test_invalid_number_two_dots()->None:
    with pytest.raises(Invalid_Number_Error):
        tokenisation("1.2.3")


def test_missing_operand_end()->None:
    tokens = tokenisation("2+")
    with pytest.raises(Missing_Operand_Error):
        validation(tokens)


def test_missing_operand_start()->None:
    tokens = tokenisation("*2")
    with pytest.raises(Missing_Operand_Error):
        validation(tokens)


def test_division_by_zero()->None:
    with pytest.raises(Division_By_Zero_Error):
        calculate([2.0, "/", 0.0])

def test_double_binary_operator()->None:
    tokens = tokenisation("2*/3")
    with pytest.raises(Missing_Operand_Error):
        validation(tokens)
