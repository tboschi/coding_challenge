import timeit
from collections import Counter
from functools import reduce
import operator

def factors(n):
    """ generator of prime factors of n """
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
    """ generator of proper divisors of n
        (excluding 1 and n)
    """
    #yield 1
    i = 2
    while i * i < n:
        if n % i == 0:
            yield i
            yield n // i
        i += 1
    if i * i == n:
        yield i


def d(n) -> int:
    """ sum of proper divisors of n """

    # get prime factorization of n = {p: m}
    fact = Counter(factors(n))

    # sum of all the divisors can be decomposed as
    # prod ( 1 + p + p² + ...)
    # where prod is on p, sum is from 0 to m
    # geometric sum ( p^k ) for k = 0, .., m
    # is = ( p^(m+1) - 1 ) / ( p - 1 )

    prod = [(p**(m+1) - 1) // (p - 1) if m > 1 else p + 1 for p, m in fact.items()]
    return reduce(operator.mul, prod, 1) - n


def solve(n = 10000) -> int:
    """ find sum of amicable numbers under n """
    checked = set()
    tot = 1
    for a in range(n+1):
        if a in checked:
            continue
        checked.add(a)

        b = d(a)
        if b == a:  # not amicable
            continue

        if d(b) == a:   # amicable
            tot += a + b    # update sum
        checked.add(b)

    return tot


if __name__ == "__main__":

    print(d(220))
    print(d(60))
    print(d(5040))
    #for i in range(1000):
        #print(f"d({i}) = {d(i)}")

    answer = solve()
    times = timeit.repeat('solve()', globals=globals(), number=1, repeat=5)
    print(f"solution {answer},\ttime (best of 5) = {1000*min(times):.6f} ms")
