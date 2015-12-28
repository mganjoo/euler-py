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


def find_min_triangle_sum(triangle_arr):
    n = len(triangle_arr)
    triangle = fill_triangle(triangle_arr)
    row_sums = np.cumsum(triangle, axis=1)
    row_sums = np.concatenate((np.zeros((n, 1)), row_sums), axis=1)

    min_sum = np.zeros((n, n))
    for i in range(n):
        kv = np.arange(i, n)
        for j in range(i + 1):
            min_sum[i, j] = ((row_sums[kv, kv - i + j + 1] - row_sums[kv, j])
                             .cumsum().min())

    return min_sum.min()


# Debug tool
def pretty_print_matrix(matrix):
    sys.stdout.write("Matrix:\n")
    for row in matrix:
        for c in row:
            sys.stdout.write("{:>5} ".format(c))
        sys.stdout.write("\n")


def print_min_triangle_sum(triangle):
    print("Minimum sum is {}".format(find_min_triangle_sum(triangle)))


if __name__ == "__main__":
    sample_triangle_mini = [[14],
                            [-15, -7],
                            [19, -13, -5]]
    sample_triangle = [[14],
                       [-15, -7],
                       [19, -13, -5],
                       [-4, 8, 23, -26],
                       [0, -4, -5, -18, 5],
                       [-17, 31, 2, 9, 28, 3]]
    g = random_number_gen(500500)
    large_triangle = [[next(g) for j in range(i + 1)]
                      for i in range(1000)]

    print_min_triangle_sum(sample_triangle_mini)
    print_min_triangle_sum(sample_triangle)
    print_min_triangle_sum(large_triangle)
