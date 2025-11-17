#!/usr/bin/env python3
"""
sets_example.py
GNU GPLv3 License
Demonstrates set operations in Python.
"""

def create_set():
    """Return a sample set of unique items."""
    return {1, 2, 3, 3, 4}  # duplicates are automatically removed

def add_to_set(s, value):
    """Add a value to a set."""
    s.add(value)
    return s

def find_union(set1, set2):
    """Return the union of two sets."""
    return set1 | set2

def find_intersection(set1, set2):
    """Return the intersection of two sets."""
    return set1 & set2

if __name__ == "__main__":
    s1 = create_set()
    s2 = {3, 4, 5}
    print("Set 1:", s1)
    print("Union:", find_union(s1, s2))
    print("Intersection:", find_intersection(s1, s2))
