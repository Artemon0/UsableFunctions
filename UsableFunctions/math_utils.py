"""Arithmetic and circular motion helpers."""

import math


def calculator(a: float, b: float, op: str) -> float | str:
    """
    Perform basic arithmetic operations.

    Args:
        a: First operand
        b: Second operand
        op: Operator (+, -, *, /, %, **)

    Returns:
        Result of the operation or error message
    """
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "**": lambda x, y: x**y,
    }

    if op in operations:
        return operations[op](a, b)
    elif op in ("/", "%"):
        try:
            return a / b if op == "/" else a % b
        except ZeroDivisionError:
            return "Error: Division by zero"

    return "Invalid operator"


def even_odd(number: int) -> str:
    """Check if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"


def factorial(n: int) -> str | int:
    """Calculate factorial recursively."""
    if n < 0:
        return "Undefined for negative numbers"
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def math_factorial(n: int) -> int:
    """Calculate factorial using math library."""
    return math.factorial(n)


def while_calculator() -> None:
    """Run an interactive calculator in a loop."""
    print("Welcome to the While Calculator!")
    print("Type 'exit' to quit.")

    while True:
        a_input = input("Enter first number: ")
        if a_input.lower() == "exit":
            break

        op = input("Enter operator (+, -, *, /, %, **): ")
        if op.lower() == "exit":
            break

        b_input = input("Enter second number: ")
        if b_input.lower() == "exit":
            break

        try:
            a = float(a_input)
            b = float(b_input)
            result = calculator(a, b, op)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")


class Circle:
    """Helper class for circle-related calculations."""

    def __init__(self, radius: float = 0, T: float = 0, N: float = 0, t: float = 0):
        """
        Initialize Circle with parameters.

        Args:
            radius: Circle radius
            T: Period
            N: Number of rotations
            t: Time
        """
        self.radius = radius
        self.T = T
        self.N = N
        self.t = t

    def calculate_v(self, radius: float, T: float) -> float:
        """Calculate velocity (circumference)."""
        return 2 * math.pi * radius

    def calculate_T(self, t: float = 0, N: float = 0, n: float = 0) -> float:
        """Calculate period T."""
        if n != 0:
            return 1 / n
        return t / N if N != 0 else 0

    def calculate_n(self, N: float, t: float) -> float:
        """Calculate frequency n."""
        return N / t if t != 0 else 0

    def calculate_N(self, n: float, t: float) -> float:
        """Calculate number of rotations N."""
        return n * t

    def calculate_t(self, N: float, t: float) -> float:
        """Calculate time t."""
        return N * t if N != 0 else 0
