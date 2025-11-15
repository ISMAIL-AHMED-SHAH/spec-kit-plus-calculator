import subprocess
import sys
from io import StringIO
from decimal import Decimal
from unittest.mock import patch
from calculator import cli

def run_cli_main(*args):
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        with patch('sys.stderr', new=StringIO()) as mock_stderr:
            with patch('sys.argv', ['main.py'] + [str(arg) for arg in args]):
                try:
                    cli.main()
                except SystemExit as e:
                    # argparse exits with SystemExit, capture the exit code
                    pass
            return mock_stdout.getvalue().strip(), mock_stderr.getvalue().strip()

def test_cli_add():
    stdout, stderr = run_cli_main("add", Decimal('10'), Decimal('5'))
    assert stdout == "15"
    assert stderr == ""

def test_cli_subtract():
    stdout, stderr = run_cli_main("subtract", Decimal('10'), Decimal('5'))
    assert stdout == "5"
    assert stderr == ""

def test_cli_multiply():
    stdout, stderr = run_cli_main("multiply", Decimal('10'), Decimal('5'))
    assert stdout == "50"
    assert stderr == ""

def test_cli_divide():
    stdout, stderr = run_cli_main("divide", Decimal('10'), Decimal('5'))
    assert stdout == "2"
    assert stderr == ""

def test_cli_divide_by_zero():
    stdout, stderr = run_cli_main("divide", Decimal('10'), Decimal('0'))
    assert stdout == "Error: Division by zero is not allowed."
    assert stderr == ""

def test_cli_no_arguments():
    stdout, stderr = run_cli_main()
    assert "usage: main.py" in stdout
    assert "Available commands" in stdout
    assert stderr == ""

def test_main_entry_point():
    # Run main.py with coverage
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "--parallel-mode", "--source=src", "src/main.py"],
        capture_output=True,
        text=True,
        check=False
    )
    assert "usage: main.py" in result.stdout.strip()
    assert "Available commands" in result.stdout.strip()
    assert result.stderr.strip() == ""
