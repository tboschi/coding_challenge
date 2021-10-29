#! /bin/python3

from collections import Counter


def factors(n):
    """generator of prime factors of n"""
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            yield i
        else:
            i += 1
    if n > 1:
        yield n


def divisors(n):
    """generator of proper divisors of n
    (excluding 1 and n)
    """
    # yield 1
    i = 2
    while i * i < n:
        if n % i == 0:
            yield i
            yield n // i
        i += 1
    if i * i == n:
        yield i


def d(n) -> int:
    """sum of proper divisors of n"""

    # get prime factorization of n = {p: m}
    fact = Counter(factors(n))

    # sum of all the divisors can be decomposed as
    # prod ( 1 + p + p² + ...)
    # where prod is on p, sum is from 0 to m
    # geometric series ( p^k ) for k = 0, .., m
    # is = ( p^(m+1) - 1 ) / ( p - 1 )

    tot = 1
    for p, m in fact.items():
        tot *= (p ** (m + 1) - 1) // (p - 1) if m > 1 else p + 1
    return tot - n


def solve(n=10000, verb=False) -> int:
    """find sum of amicable numbers under n"""
    checked = set()
    tot = 0
    for a in range(2, n + 1):
        if a in checked:
            continue
        checked.add(a)

        b = d(a)
        if b == a:  # not amicable
            if verb:
                print(f"{a} is perfect")
            continue

        if d(b) == a:  # amicable
            if verb:
                print(f"{a} and {b} are amicable")
            tot += a + b  # update sum
        checked.add(b)

    return tot


if __name__ == "__main__":

    print("Finding amicable numbers under 1e5")
    solve(100000, True)
