"""
Simple Command-Line Calculator
Syntecxhub Week 1 - Project 1
Author: Ananya
Description: Performs basic arithmetic with error handling.
Accepts input with or without spaces: 10+5 or 10 + 5
"""

import re

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate() -> None:
    """
    Run the main calculator loop.
    Accepts user input in format: number operator number
    Examples: 10+5, 20 / 4, 8*3
    Supports: +, -, *, / and commands 'clear' and 'exit'
    """
    operations = {'+': add, '-': subtract, '*': multiply, 'x': multiply, '/': divide}

    while True:
        print("\n--- Simple Calculator ---")
        print("Operators: + - * / | 'clear' to reset | 'exit' to quit")
        user_input = input("Enter calculation: ").strip().lower()

        if user_input == 'exit':
            print("Exiting Calculator. Goodbye!")
            break
        if user_input == 'clear':
            continue

        try:
            # Use regex to split numbers and operators. Works with/without spaces
            # Matches: 10, 10.5, +, -, *, /, x
            parts = re.findall(r'\d+\.?\d*|[+\-*/x]', user_input)

            if len(parts)!= 3:
                print("Invalid format. Examples: 10 + 5 or 10+5")
                continue

            num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

            if op not in operations:
                print("Invalid operator. Use +, -, *, /")
                continue

            result = operations[op](num1, num2)
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Please enter numbers and operator only.")

# Start the calculator
if __name__ == "__main__":
    calculate()
