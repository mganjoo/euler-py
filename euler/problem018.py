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


def full(data_path):
    return [read_triangle(triangle_file)]
