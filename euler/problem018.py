# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23
# Find the maximum total from top to bottom of the triangle below


def solution(triangle):
    h = len(triangle)
    max_sum = [[0 for j in range(i + 1)] for i in range(h - 1)]
    max_sum.append([triangle[h - 1][j] for j in range(h)])
    for i in range(h - 2, -1, -1):
        for j in range(0, i + 1):
            max_sum[i][j] = (triangle[i][j] +
                             max(max_sum[i + 1][j], max_sum[i + 1][j + 1]))

    return max_sum[0][0]


def read_triangle(filename):
    with open(filename) as f:
        return [[int(n) for n in line.split()] for line in f]


def test_cases(*args):
    tri = [[3],
           [7, 4],
           [2, 4, 6],
           [8, 5, 9, 3]]
    return [([tri], 23)]


def args(resource_accessor):
    return [read_triangle(resource_accessor.resource_filename("triangle.txt"))]
