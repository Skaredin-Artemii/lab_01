"""calculator.py"""
from typing import Union

from .errors import (
    Division_By_Zero_Error,
    Double_Operator_Error,
    Empty_Expression_Error,
    Invalid_Number_Error,
    Missing_Operand_Error,
    Unknown_Symbol_Error,
)

Token=Union[float,str]
"""Tokenisation"""
def tokenisation(expr:str) -> list[Token]:
    if expr is None or all(c == " " for c in expr):
        raise Empty_Expression_Error()

    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue

        if i + 1 < len(expr) and expr[i:i+2] == '//':
            tokens.append(expr[i:i+2])
            i += 2
            continue

        if expr[i] in '+-':
            j = i - 1
            while j >= 0 and expr[j] == ' ':
                j -= 1
            pred = expr[j] if j >= 0 else None
            k = i + 1
            while k < len(expr) and expr[k] == ' ':
                k += 1
            is_unary = pred is None or pred in '+-*/%'
            if is_unary and k < len(expr) and (expr[k].isdigit() or expr[k] == '.'):
                num = expr[i]
                i = k
                while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                    num += expr[i]
                    i += 1
                if num.count('.') > 1:
                    raise Invalid_Number_Error("некорректная запись числа: " + num)
                tokens.append(float(num))
                continue
            else:
                tokens.append(expr[i])
                i += 1
                continue

        if expr[i] in '*/%':
            tokens.append(expr[i])
            i += 1
            continue

        if expr[i].isdigit() or expr[i] == '.':
            num = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            if num.count('.') > 1:
                raise Invalid_Number_Error("некорректная запись числа: " + num)
            tokens.append(float(num))
            continue

        raise Unknown_Symbol_Error("неизвестный символ: " + expr[i])

    return tokens
"""Validation"""

def validation(tokens:list[Token])->None:
    if not tokens:
        raise Empty_Expression_Error()

    j = 0
    while j < len(tokens):
        t = tokens[j]
        is_num = isinstance(t, float)

        if j % 2 == 0 and not is_num:
            raise Missing_Operand_Error("ожидалось число, получено: " + str(t))
        if j % 2 != 0 and is_num:
            raise Double_Operator_Error("ожидалось действие, получено: " + str(t))
        j += 1
    if not isinstance(tokens[-1], float):
        raise Missing_Operand_Error("выражение не может заканчиваться оператором")

"""Calculation"""
def calculate(tokens: list[Token])->float:
    tokens = tokens[:]

    i = 0
    while i < len(tokens):
        if tokens[i] in ('*', '/', '%', '//'):
            a = tokens[i-1]
            b = tokens[i+1]
            if tokens[i] == '*':
                res = a * b
            elif tokens[i] == '/':
                if b == 0:
                    raise Division_By_Zero_Error("Деление на 0")
                res = a / b
            elif tokens[i] == '%':
                if b == 0:
                    raise Division_By_Zero_Error("Деление на 0")
                res = a % b
            else:  # '//'
                if b == 0:
                    raise Division_By_Zero_Error("Деление на 0")
                res = a // b
            tokens[i-1] = res
            del tokens[i:i+2]
            i = 0
            continue
        i += 1

    i = 0
    while i < len(tokens):
        if tokens[i] in ('+', '-'):
            a = tokens[i-1]
            b = tokens[i+1]
            if tokens[i] == '+':
                res = a + b
            else:
                res = a - b
            tokens[i-1] = res
            del tokens[i:i+2]
            i = 0
            continue
        i += 1

    return tokens[0]
