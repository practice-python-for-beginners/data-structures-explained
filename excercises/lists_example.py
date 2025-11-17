#!/usr/bin/env python3
"""
lists_example.py
GNU GPLv3 License
Covers basic list operations in Python.
"""

def create_list():
    """Return a sample list of integers."""
    return [1, 2, 3, 4, 5]

def append_to_list(lst, value):
    """Append a value to a list and return it."""
    lst.append(value)
    return lst

def remove_from_list(lst, value):
    """Remove the first occurrence of value from a list."""
    if value in lst:
        lst.remove(value)
    return lst

def sort_list(lst):
    """Return a sorted copy of the provided list."""
    return sorted(lst)

if __name__ == "__main__":
    numbers = create_list()
    print("Original:", numbers)
    print("After append:", append_to_list(numbers, 6))
    print("After remove:", remove_from_list(numbers, 2))
    print("Sorted copy:", sort_list(numbers))
