#! /bin/python3


def solve(n=4e6, verb=False):
    """sum the even Fibonacci values under n"""
    f0, f1 = 0, 1
    tot = 0
    while f1 <= n:
        if f1 % 2 == 0:
            tot += f1

        # update
        if verb:
            print(f"{f1} -> {tot}")
        f0, f1 = f1, f0 + f1

    return tot


if __name__ == "__main__":
    tot = solve(4e6, True)
    print("solution", tot)
