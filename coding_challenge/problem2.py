#! /bin/python3

import math

voca = {1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        20 : 'twenty',
        30 : 'thirty',
        40 : 'forty',
        50 : 'fifty',
        60 : 'sixty',
        70 : 'seventy',
        80 : 'eighty',
        90 : 'ninety',
        100 : 'hundred',
        1000 : 'thousand'}

def to_string(unit):
    if unit > 9999:
        raise ValueError("range accepted 0-9999")

    if not unit:
        return 'zero'

    if unit < 100 and unit in voca:
        return voca[unit]

    mag = int(math.log10(unit))

    msb = unit // 10**mag
    gross = msb * 10**mag
    if gross < 100 and gross in voca:
        letters = voca[gross]
    else:
        letters = voca[msb] + " " + voca[10**mag] if msb else ""

    unit -= gross
    if not unit:
        return letters

    if mag > 2:
        if unit < 100:
            sep = " and "
        else:
            sep = ", "
    elif mag == 2:
        sep = " and "
    else:
        sep = "-"
    return letters + sep + to_string(unit)


def count_chars(unit):
    if unit > 9999:
        raise ValueError("range accepted 0-9999")

    if not unit:
        return 0

    if unit < 100 and unit in voca:
        return len(voca[unit])

    mag = int(math.log10(unit))

    msb = unit // 10**mag
    gross = msb * 10**mag
    if gross < 100 and gross in voca:
        chars = len(voca[gross])
    else:
        chars = len(voca[msb] + voca[10**mag]) if msb else 0

    unit -= gross
    if not unit:
        return chars

    sep = 0
    if (mag > 2 and unit < 100) or mag == 2:
        sep = 3 # "and"

    return chars + sep + count_chars(unit)


def solve():
    return sum(count_chars(i+1) for i in range(1000))


if __name__ == "__main__":

    solution = solve()
    print(f"Solution to problem 2 is {solution}")
