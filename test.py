#! /bin/python3

import timeit

from codingchallenge import problem1 as p1
from codingchallenge import problem2 as p2
from codingchallenge import problem3 as p3
from codingchallenge import problem4 as p4
from codingchallenge import problem5 as p5
from codingchallenge import problem6 as p6
from codingchallenge import problem7 as p7

challenge = {'problem 1' : p1,
             'problem 2' : p2,
             'problem 3' : p3,
             'problem 4' : p4,
             'problem 5' : p5,
             'problem 6' : p6,
             'problem 7' : p7}

for name, lib in challenge.items():
    answer = lib.solve()
    times = timeit.repeat('lib.solve()', globals=globals(), number=1, repeat=5)
    print(f"{name}: solution {answer},\ttime (best of 5) = {1000*min(times):.6f} ms")
