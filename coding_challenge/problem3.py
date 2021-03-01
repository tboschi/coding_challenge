#! /bin/python3

def load(file_input):
    triangle = []
    with open(file_input) as f:
        for line in f:
            lvl = [int(i) for i in line.split()]
            triangle.append(lvl)

    return triangle


def solve(file_input = 'triangle.txt'):
    triangle = load(file_input)

    path = triangle[0][0]
    i = 0
    for lvl in triangle[1:]:
        if lvl[i] < lvl[i+1]:
            i += 1

        path += lvl[i]

    return path

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 1:
        print("Input file expected", file=sys.stderr)
        sys.exit(1)

    solution = solve(sys.argv[1])
    print(f"Solution to problem 3 is {solution}")
