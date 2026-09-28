"""Тесты CLI через subprocess."""

import subprocess
import sys


def run_cli(*args:str)->tuple[int,str,str]:

    result = subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def test_cli_calc_ok()->None:
    code, out, err = run_cli("calc", "2+2*2")
    assert code == 0
    assert out == "6.0"
    assert err == ""


def test_cli_convert_ok()->None:
    code, out, err = run_cli("convert", "5", "--from", "km", "--to", "m")
    assert code == 0
    assert out == "5000.0"
    assert err == ""


def test_cli_calc_error()->None:
    code, out, err = run_cli("calc", "2/0")
    assert code == 2
    assert out == ""
    assert "Ошибка" in err


def test_cli_convert_error()->None:
    code, out, err = run_cli("convert", "5", "--from", "km", "--to", "kg")
    assert code == 2
    assert out == ""
    assert "Ошибка" in err


def test_cli_help_exit_zero() -> None:
    code, out, err = run_cli("--help")
    assert code == 0
    assert "toolkit" in out.lower()
