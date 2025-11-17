#!/usr/bin/env python3
"""
tuples_example.py
GNU GPLv3 License
Covers tuple creation, unpacking, and access.
"""

def create_tuple():
    """Return a sample tuple."""
    return ("Python", 3.11, "Beginner")

def access_tuple(tpl, index):
    """Return an element at the given index."""
    return tpl[index]

def unpack_tuple(tpl):
    """Unpack the elements of a tuple into individual variables."""
    name, version, level = tpl
    return f"{name} version {version} for {level} learners"

if __name__ == "__main__":
    t = create_tuple()
    print("Tuple:", t)
    print("Access index 1:", access_tuple(t, 1))
    print("Unpacked:", unpack_tuple(t))
