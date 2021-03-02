#! /bin/python3

def solve(n = 4e6, verb = False):
    """ sum the even fibonacci values under n """
    f0, f1, fn = 0, 1, 1
    tot = 0
    while fn < n:
        if fn % 2 == 0:
            tot += fn

        # update
        if verb:
            print(f"{fn} -> {tot}")
        f0, f1, fn = f1, fn, f1 + fn

    return tot


if __name__ == "__main__":
    solve(4e6, True)
