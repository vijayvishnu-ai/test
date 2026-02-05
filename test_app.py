"""
Tests for the Python test application.
"""
import pytest
from app import Calculator, StringUtils, ListUtils


class TestCalculator:
    """Tests for the Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """Test subtraction."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(3.5, 1.5) == 2.0

    def test_multiply(self):
        """Test multiplication."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(1.5, 2) == 3.0

    def test_divide(self):
        """Test division."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-6, 2) == -3
        assert self.calc.divide(0, 5) == 0

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)


class TestStringUtils:
    """Tests for the StringUtils class."""

    def test_reverse(self):
        """Test string reversal."""
        assert StringUtils.reverse("hello") == "olleh"
        assert StringUtils.reverse("a") == "a"
        assert StringUtils.reverse("") == ""
        assert StringUtils.reverse("12345") == "54321"

    def test_is_palindrome(self):
        """Test palindrome detection."""
        assert StringUtils.is_palindrome("radar") is True
        assert StringUtils.is_palindrome("Radar") is True
        assert StringUtils.is_palindrome("race car") is True
        assert StringUtils.is_palindrome("hello") is False
        assert StringUtils.is_palindrome("a") is True
        assert StringUtils.is_palindrome("") is True

    def test_word_count(self):
        """Test word counting."""
        assert StringUtils.word_count("hello world") == 2
        assert StringUtils.word_count("one") == 1
        assert StringUtils.word_count("") == 0
        assert StringUtils.word_count("   ") == 0
        assert StringUtils.word_count("  multiple   spaces  ") == 2


class TestListUtils:
    """Tests for the ListUtils class."""

    def test_find_max(self):
        """Test finding maximum value."""
        assert ListUtils.find_max([1, 2, 3, 4, 5]) == 5
        assert ListUtils.find_max([-5, -1, -10]) == -1
        assert ListUtils.find_max([42]) == 42
        assert ListUtils.find_max([1.5, 2.5, 0.5]) == 2.5

    def test_find_max_empty_list(self):
        """Test find_max raises ValueError for empty list."""
        with pytest.raises(ValueError, match="List cannot be empty"):
            ListUtils.find_max([])

    def test_find_min(self):
        """Test finding minimum value."""
        assert ListUtils.find_min([1, 2, 3, 4, 5]) == 1
        assert ListUtils.find_min([-5, -1, -10]) == -10
        assert ListUtils.find_min([42]) == 42
        assert ListUtils.find_min([1.5, 2.5, 0.5]) == 0.5

    def test_find_min_empty_list(self):
        """Test find_min raises ValueError for empty list."""
        with pytest.raises(ValueError, match="List cannot be empty"):
            ListUtils.find_min([])

    def test_average(self):
        """Test average calculation."""
        assert ListUtils.average([1, 2, 3, 4, 5]) == 3.0
        assert ListUtils.average([10]) == 10.0
        assert ListUtils.average([0, 0, 0]) == 0.0
        assert ListUtils.average([1, 2]) == 1.5

    def test_average_empty_list(self):
        """Test average raises ValueError for empty list."""
        with pytest.raises(ValueError, match="List cannot be empty"):
            ListUtils.average([])
