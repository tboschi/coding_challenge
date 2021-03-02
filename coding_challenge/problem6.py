def solve(n = 4000000):
    """ sum of even fibonacci values under n """
    f0, f1 = 1, 2
    fib = f0 + f1

    tot = 2
    while fib < n:
        if fib % 2 == 0:
            tot += fib

        # update
        f0 = f1
        f1 = fib
        fib = f0 + f1

    return tot


if __name__ == "__main__":
    print(solve())
