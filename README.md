# Coding challenge by SG

The solutions to problems 1-6 are structured as the `coding_challenge` package.
Each problem has its own module, named `problemX`, where `X` is the problem number.
The method `solve` is available in each module and it returns the correct answer.

All problems can be tested at once with
```
python test.py
```
which prints not only the answers to each problem, but also the execution time in milliseconds (best of 5 runs).

## Solutions

This is the output of `test.py` on my system (Linux + AMD Ryzen 4000)
```
problem 1: solution 376,	time (best of 5) = 8.184685 ms
problem 2: solution 21124,	time (best of 5) = 1.556899 ms
problem 3: solution 1064,	time (best of 5) = 0.027657 ms
problem 4: solution 1533776805,	time (best of 5) = 11.024844 ms
problem 5: solution 31626,	time (best of 5) = 54.881875 ms
problem 6: solution 4613732,	time (best of 5) = 0.003842 ms
problem 7: solution 26033,	time (best of 5) = 10015.359399 ms
```

N.B. the solution to problem 3 differs from the result posted on the instructions (1064 vs 1074). I believe this is a typo of the problem description, as I checked the result by hand as well.
