"""
A simple Python test application with various utility functions.
"""


class Calculator:
    """A basic calculator class with arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class StringUtils:
    """Utility class for string operations."""

    @staticmethod
    def reverse(s: str) -> str:
        """Reverse a string."""
        return s[::-1]

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """Check if a string is a palindrome (case-insensitive)."""
        cleaned = s.lower().replace(" ", "")
        return cleaned == cleaned[::-1]

    @staticmethod
    def word_count(s: str) -> int:
        """Count the number of words in a string."""
        if not s.strip():
            return 0
        return len(s.split())


class ListUtils:
    """Utility class for list operations."""

    @staticmethod
    def find_max(numbers: list) -> float:
        """Find the maximum value in a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        return max(numbers)

    @staticmethod
    def find_min(numbers: list) -> float:
        """Find the minimum value in a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        return min(numbers)

    @staticmethod
    def average(numbers: list) -> float:
        """Calculate the average of a list of numbers."""
        if not numbers:
            raise ValueError("List cannot be empty")
        return sum(numbers) / len(numbers)


def main():
    """Demonstrate the functionality of the application."""
    calc = Calculator()
    print("Calculator Demo:")
    print(f"  5 + 3 = {calc.add(5, 3)}")
    print(f"  10 - 4 = {calc.subtract(10, 4)}")
    print(f"  6 * 7 = {calc.multiply(6, 7)}")
    print(f"  20 / 4 = {calc.divide(20, 4)}")

    print("\nString Utils Demo:")
    print(f"  Reverse 'hello': {StringUtils.reverse('hello')}")
    print(f"  Is 'radar' a palindrome? {StringUtils.is_palindrome('radar')}")
    print(f"  Word count of 'hello world': {StringUtils.word_count('hello world')}")

    print("\nList Utils Demo:")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"  Numbers: {numbers}")
    print(f"  Max: {ListUtils.find_max(numbers)}")
    print(f"  Min: {ListUtils.find_min(numbers)}")
    print(f"  Average: {ListUtils.average(numbers)}")


if __name__ == "__main__":
    main()
