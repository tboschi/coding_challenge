#! /bin/python3

import math

def triangular(n) -> int:
    """ n-th triangular number"""
    # diff between consecutive numbers is (n+1)
    return n * (n + 1) // 2

# n^2 + n - 2x = 0 -> solve
# n = (sqrt(1 + 8 x) - 1) / 2

def is_triangular(n) -> bool:
    """ check if n is triangular"""
    return (((math.sqrt(1 + 8 * n) - 1) / 2) % 1 == 0)

def where_triangular(n) -> int:
    """ return lower bound number for closest triangular number to n"""
    return int((math.sqrt(1 + 8 * n) - 1) / 2)


def pentagonal(n) -> int:
    """ n-th pentagonal number"""
    # diff between consecutive numbers is (3n+1)
    return n * (3 * n - 1) // 2

# 3 n^2 - n - 2x = 0
# n = (sqrt(1 + 24 x) + 1) / 6

def is_pentagonal(n) -> bool:
    """ check if n is pentagonal"""
    return (((math.sqrt(1 + 24 * n) + 1) / 6) % 1 == 0)

def where_pentagonal(n) -> int:
    """ return lower bound number for closest pentagonal number to n"""
    return int((math.sqrt(1 + 24 * n) + 1) / 6)


def hexagonal(n) -> int:
    # diff between consecutive numbers is (4n+1)
    return n * (2 * n - 1)

# 2 n^2 - n - x = 0
# n = (sqrt(1 + 8 x) + 1) / 4

def is_hexagonal(n) -> bool:
    """ check if n is hexagonal"""
    return (((math.sqrt(1 + 8 * n) + 1) / 4) % 1 == 0)

def where_hexagonal(n) -> int:
    """ return lower bound number for closest hexagonal number to n"""
    return int((math.sqrt(1 + 8 * n) + 1) / 4)


def solve(n = 143):
    """ 2m-1 triangular numbers are also hexagonal,
    so any hexagonal number is automatically triangular
    this routine only checks if hexagonal numbers are pentagonal
    return which 3-tuple of triangular, pentagonal, hexagonal entries
    starting from n-th hexagonal number
    143rd hexagonal number is the first number
    also triangular and pentagonal (285th and 165th)
    so starting from 144
    """

    while True:
        n += 1
        x = hexagonal(n)
        if is_pentagonal(x):
            return x


if __name__ == "__main__":

    print("Finding triangular+pentagonal+hexagonal numbers under 1e7")
    n = 0
    while n < 1e7:
        n += 1
        x = hexagonal(n)
        if is_pentagonal(x):
            t, p, h = where_triangular(x), where_pentagonal(x), n

            print(f"Number {triangular(t)} is a triangular ({t}), "
                  f"pentagonal ({p}), and hexagonal ({h}) number")
