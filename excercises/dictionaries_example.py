#!/usr/bin/env python3
"""
dictionaries_example.py
GNU GPLv3 License
Shows basic dictionary creation and manipulation.
"""

def create_dict():
    """Return a sample dictionary."""
    return {"name": "Alice", "age": 25, "city": "Paris"}

def add_entry(dct, key, value):
    """Add a new key-value pair to a dictionary."""
    dct[key] = value
    return dct

def remove_entry(dct, key):
    """Remove a key from a dictionary if it exists."""
    if key in dct:
        del dct[key]
    return dct

def get_value(dct, key):
    """Return the value associated with a key, or None if not found."""
    return dct.get(key)

if __name__ == "__main__":
    person = create_dict()
    print("Dictionary:", person)
    print("After adding country:", add_entry(person, "country", "France"))
    print("After removing age:", remove_entry(person, "age"))
    print("Name:", get_value(person, "name"))
