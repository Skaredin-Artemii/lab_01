"""__main__.py"""

import argparse
import sys

from .calculator import calculate, tokenisation, validation
from .converter import convert
from .errors import Toolkit_Error


def main()-> None:
    parser = argparse.ArgumentParser(prog="toolkit", description="Калькулятор и конвертер")
    sub = parser.add_subparsers(dest="command")

    p_calc = sub.add_parser("calc", help="Вычислить выражение")
    p_calc.add_argument("expression")

    p_conv = sub.add_parser("convert", help="Конвертировать величину")
    p_conv.add_argument("value", type=float)
    p_conv.add_argument("--from", dest="src", required=True)
    p_conv.add_argument("--to", dest="dst", required=True)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    try:
        if args.command == "calc":
            tokens = tokenisation(args.expression)
            validation(tokens)
            result = calculate(tokens)
        else:
            result = convert(args.value, args.src, args.dst)
    except Toolkit_Error as e:
        print("Ошибка:", e, file=sys.stderr)
        sys.exit(2)

    print(result)
    sys.exit(0)


if __name__ == "__main__":
    main()
