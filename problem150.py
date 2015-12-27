import sys


def rng(n):
    t = 0
    mask = (2 << 20) - 1
    sub = 1 << 19
    for k in range(n + 1):
        t = (615949 * t + 797807) & mask
        yield t - sub


def find_min_sum_triangle(triangle):
    n = len(triangle)

    vertical_sums = [triangle[0]]
    for i in range(1, n):
        vertical_sums.append([triangle[i][j] + vertical_sums[i - 1][j]
                              for j in range(n)])

    diagonal_sums = [[0] * i +
                     [triangle[i][0]] + [0] * (n - i - 1) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            diagonal_sums[i][j] = diagonal_sums[i][j - 1] + triangle[j][j - i]

    triangle_sums = [[[0] * n for i in range(n)] for j in range(n)]

    for j in range(n):
        triangle_sums[0][j][0] = sum(vertical_sums[j][t] for t in range(n))
    for i in range(1, n):
        for j in range(i, n):
            triangle_sums[i][j][0] = (triangle_sums[i - 1][j][0] -
                                      diagonal_sums[i - 1][j])
            for k in range(1, i + 1):
                subtr = (vertical_sums[j][k - 1] -
                         (vertical_sums[i - 2][k - 1] if i >= 2 else 0))
                triangle_sums[i][j][k] = triangle_sums[i - 1][j][k - 1] - subtr

    min_sum = sys.maxint
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if triangle_sums[i][j][k] < min_sum:
                    min_sum = triangle_sums[i][j][k]
                    min_i, min_j, min_k = i, j, k

    print(min_i, min_j, min_k)
    return min_sum


def pretty_print_matrix(matrix):
    sys.stdout.write("Matrix:\n")
    for line in matrix:
        for c in line:
            sys.stdout.write("{:>5} ".format(c))
        sys.stdout.write("\n")

if __name__ == "__main__":
    # with open("problem150_sample.txt") as f:
    #     n = int(f.readline())
    #     triangle = []
    #     for i in range(n):
    #         triangle.append([0] * n)
    #         for j in range(i + 1):
    #             triangle[i][j] = int(f.readline())

    # print("Minimum sum is {}".format(find_min_sum_triangle(triangle)))
    triangle = [[0] * 1000 for _ in range(1000)]
    for x in rng(500500):
        for i in range(1000):
            for j in range(i + 1):
                triangle[i][j] = x

    print("Minimum sum is {}".format(find_min_sum_triangle(triangle)))
