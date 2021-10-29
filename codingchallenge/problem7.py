from functools import cache


def gen_primes():
    """indefinite generator of prime numbers using the sieve of Eratosthenes"""

    # dictionary with next number to skip
    # following a 'sieve line' of a prime number
    P = {}
    q = 2  # start with 2
    while True:
        if q not in P:  # is prime
            yield q
            P[q + q] = q  # next number to skip is q+q (from q prime number)
        else:  # q is not prime
            n = q + P[q]  # next number to skip
            while n in P:  # add prime until new number not in dict is found
                n += P[q]
            P[n] = P[q]  # add it, coming from same prime number
            del P[q]  # remove old entry

        q += 1


# LRU caching with indefinite size
@cache
def is_prime(n: int) -> bool:
    """primality test with 6k±1 optimization"""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def cat_prime(a, b) -> bool:
    """if 'a', 'b', check if 'ab' and 'ba' are also prime
    a   is prime int or collection of prime int
    b   must be prime number
    """
    try:  # check if a is iterable
        it = iter(a)
    except:  # it is not, treat as int
        return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))
    else:  # must cat_prime with all elements
        return all(cat_prime(p, b) for p in a)


def solve(n=5, tup=False):
    """find first n-tuple of prime numbers with the following property:
    any two of those n primes can be concatenated in any order to
    form another prime.
    e.g.  7 and 109 form 7109 or 1097 and both are prime
    return the sum of those n prime numbers
    """

    primer = gen_primes()

    primes = []
    tuples = []
    while True:
        p = next(primer)
        if p == 2 or p == 5:
            continue

        # check in collected tuples if any can be extended
        for t in tuples:
            if cat_prime(t, p):
                tuples.append(t[:] + [p])
        # check among known prime numbers
        # for new tuples
        for c in primes:
            if cat_prime(c, p):
                tuples.append([c, p])

        # store prime number
        primes.append(p)

        # if any tuple is of desirable length, return
        for t in tuples:
            if len(t) == n:
                return t if tup else sum(t)


if __name__ == "__main__":

    s2 = solve(2, True)
    print(f"First couple of special primes is {s2} (sum = {sum(s2)})")

    s3 = solve(3, True)
    print(f"First triple of special primes is {s3} (sum = {sum(s3)})")

    s4 = solve(4, True)
    print(f"First quadruple of special primes is {s4} (sum = {sum(s4)})")

    s5 = solve(5, True)
    print(f"First quintuple of special primes is {s5} (sum = {sum(s5)})")
