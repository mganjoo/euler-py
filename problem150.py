import sys


def zeros(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def random_number_gen(n):
    t = 0
    mask = (1 << 20) - 1
    sub = 1 << 19
    for k in range(n + 1):
        t = (615949 * t + 797807) & mask
        yield t - sub


def fill_triangle(triangle):
    n = len(triangle)
    for i in range(n):
        triangle[i] += [0] * (n - i - 1)


def find_min_triangle_sum(triangle):
    fill_triangle(triangle)

    n = len(triangle)

    row_sums = zeros(n)
    for i in range(n):
        row_sums[i][0] = triangle[i][0]
        for j in range(1, n):
            row_sums[i][j] = row_sums[i][j - 1] + triangle[i][j]

    min_sum = sys.maxsize
    for i in range(n):
        for j in range(i + 1):
            cur_sum = 0
            for k in range(i, n):
                cur_sum += (row_sums[k][k - i + j] -
                            (row_sums[k][j - 1] if j > 0 else 0))
                min_sum = min(cur_sum, min_sum)

    return min_sum


def pretty_print_matrix(matrix):
    sys.stdout.write("Matrix:\n")
    for line in matrix:
        for c in line:
            sys.stdout.write("{:>5} ".format(c))
        sys.stdout.write("\n")


def print_min_triangle_sum(triangle):
    print("Minimum sum is {}".format(find_min_triangle_sum(triangle)))


if __name__ == "__main__":
    sample_triangle = [[15],
                       [-14, -7],
                       [20, -13, -5],
                       [-3, 8, 23, -26],
                       [1, -4, -5, -18, 5],
                       [-16, 31, 2, 9, 28, 3]]
    g = random_number_gen(500500)
    large_triangle = [[next(g) for j in range(i + 1)] for i in range(1000)]

    print_min_triangle_sum(sample_triangle)
    print_min_triangle_sum(large_triangle)
