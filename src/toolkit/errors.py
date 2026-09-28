"""errors.py -исключения тулкита"""
class Toolkit_Error(Exception):
    pass
"""Калькулятор"""
class Calculator_Error(Toolkit_Error):
    pass
class Empty_Expression_Error(Calculator_Error):
    pass
class Unknown_Symbol_Error(Calculator_Error):
    pass
class Invalid_Number_Error(Calculator_Error):
    pass
class Missing_Operand_Error(Calculator_Error):
    pass
class Double_Operator_Error(Calculator_Error):
    pass
class Division_By_Zero_Error(Calculator_Error):
    pass
"""Конвертер"""
class Converter_Error(Toolkit_Error):
    pass
class Unknown_Unit_Error(Converter_Error):
    pass
class Incompatible_Units_Error(Converter_Error):
    pass
class Below_Absolute_Zero_Error(Converter_Error):
    pass
"""CLI"""
class CLI_Error(Toolkit_Error):
    pass
class Invalid_Value_Error(CLI_Error):
    pass
