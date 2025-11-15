import argparse
from decimal import Decimal
from calculator import operations

def main():
    """Main function for the calculator CLI.

    Parses command-line arguments and performs the specified arithmetic operation.
    Handles addition, subtraction, multiplication, and division.
    Prints the result or an error message for division by zero.
    """
    parser = argparse.ArgumentParser(description="A simple calculator CLI.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("num1", type=Decimal, help="The first number")
    add_parser.add_argument("num2", type=Decimal, help="The second number")

    # Subtract command
    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers")
    subtract_parser.add_argument("num1", type=Decimal, help="The first number")
    subtract_parser.add_argument("num2", type=Decimal, help="The second number")

    # Multiply command
    multiply_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    multiply_parser.add_argument("num1", type=Decimal, help="The first number")
    multiply_parser.add_argument("num2", type=Decimal, help="The second number")

    # Divide command
    divide_parser = subparsers.add_parser("divide", help="Divide two numbers")
    divide_parser.add_argument("num1", type=Decimal, help="The first number")
    divide_parser.add_argument("num2", type=Decimal, help="The second number")

    args = parser.parse_args()

    if args.command == "add":
        result = operations.add(args.num1, args.num2)
        print(result)
    elif args.command == "subtract":
        result = operations.subtract(args.num1, args.num2)
        print(result)
    elif args.command == "multiply":
        result = operations.multiply(args.num1, args.num2)
        print(result)
    elif args.command == "divide":
        try:
            result = operations.divide(args.num1, args.num2)
            print(result)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    else:
        parser.print_help()
