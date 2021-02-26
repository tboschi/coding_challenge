#! /bin/python3

import timeit

import coding_challenge.problem1 as c1
import coding_challenge.problem2 as c2
import coding_challenge.problem3 as c3

answer = c1.solve('poker.txt')
times = timeit.repeat('c1.solve(\'poker.txt\')', globals=globals(), number=1, repeat=5)
print(f"Problem 1: solution {answer}, time (best of 5) = {1000*min(times):.6f} ms")

answer = c2.solve()
times = timeit.repeat('c2.solve()', globals=globals(), number=1, repeat=5)
print(f"Problem 2: solution {answer}, time (best of 5) = {1000*min(times):.6f} ms")

answer = c3.solve('triangle.txt')
times = timeit.repeat('c3.solve(\'triangle.txt\')', globals=globals(), number=1, repeat=5)
print(f"Problem 3: solution {answer}, time (best of 5) = {1000*min(times):.6f} ms")
