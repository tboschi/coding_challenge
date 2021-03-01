
def solve(n = 4000000):
    """ sum of even fibonacci values under n """
    fib0 = 1
    fib1 = 2
    fib = fib0 + fib1
    tot = 2
    while fib < n:
        if fib % 2 == 0:
            tot += fib
        fib0 = fib1
        fib1 = fib
        fib = fib0 + fib1

    return tot

if __name__ == "__main__":
    
    print(solve())
