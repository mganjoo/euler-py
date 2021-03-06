# In a triangular array of positive and negative integers, we wish to find a
# sub-triangle such that the sum of the numbers it contains is the smallest
# possible.

import numpy as np
import sys


def random_number_gen(n):
    t = 0
    mask = (1 << 20) - 1
    sub = 1 << 19
    for k in range(n + 1):
        t = (615949 * t + 797807) & mask
        yield t - sub


def fill_triangle(triangle_arr):
    n = len(triangle_arr)
    for i in range(n):
        triangle_arr[i] += [0] * (n - i - 1)
    return np.array(triangle_arr)


def solution(triangle_arr):
    n = len(triangle_arr)
    triangle = fill_triangle(triangle_arr)
    row_sums = np.cumsum(triangle, axis=1)
    row_sums = np.concatenate((np.zeros((n, 1)), row_sums), axis=1)

    min_sum = np.zeros((n))

    for i in range(n):
        j = np.arange(i + 1)
        k = np.arange(i, n)
        jv, kv = np.meshgrid(j, k, indexing='ij')
        min_sum[i] = np.min(np.cumsum(
            row_sums[kv, kv - i + jv + 1] - row_sums[kv, jv], axis=1))

    return int(min_sum.min())


# Debug tool
def pretty_print_matrix(matrix):
    sys.stdout.write("Matrix:\n")
    for row in matrix:
        for c in row:
            sys.stdout.write("{:>5} ".format(c))
        sys.stdout.write("\n")


def test_cases(*args):
    triangle = [[14],
                [-15, -7],
                [19, -13, -5],
                [-4, 8, 23, -26],
                [0, -4, -5, -18, 5],
                [-17, 31, 2, 9, 28, 3]]

    return [([triangle], -42)]


def args(*args):
    g = random_number_gen(500500)
    return [[[next(g) for j in range(i + 1)]
             for i in range(1000)]]
