#!/usr/bin/env python3
"""
Main test script for GitHub PR workflow verification.
"""

def hello_world():
    """Return a greeting message."""
    return "Hello, GitHub PR World!"

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b

def main():
    """Main function to demonstrate functionality."""
    print(hello_world())
    result = add_numbers(5, 7)
    print(f"5 + 7 = {result}")
    multiply_result = multiply_numbers(3, 4)
    print(f"3 * 4 = {multiply_result}")
    return result

if __name__ == "__main__":
    main()