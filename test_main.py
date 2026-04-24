#!/usr/bin/env python3
"""
Unit tests for main.py
"""

import unittest
from main import hello_world, add_numbers, multiply_numbers

class TestMain(unittest.TestCase):
    """Test cases for main.py functions."""
    
    def test_hello_world(self):
        """Test hello_world function."""
        self.assertEqual(hello_world(), "Hello, GitHub PR World!")
    
    def test_add_numbers_positive(self):
        """Test addition with positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_add_numbers_negative(self):
        """Test addition with negative numbers."""
        self.assertEqual(add_numbers(-2, 3), 1)
    
    def test_add_numbers_zero(self):
        """Test addition with zero."""
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_add_numbers_large(self):
        """Test addition with large numbers."""
        self.assertEqual(add_numbers(1000, 2000), 3000)
    
    def test_multiply_numbers_positive(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(multiply_numbers(2, 3), 6)
    
    def test_multiply_numbers_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(multiply_numbers(5, 0), 0)
    
    def test_multiply_numbers_negative(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply_numbers(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()