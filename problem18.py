def max_path_sum(triangle):
    h = len(triangle)
    max_sum = [[0 for j in range(i + 1)] for i in range(h - 1)]
    max_sum.append([triangle[h - 1][j] for j in range(h)])
    for i in range(h - 2, -1, -1):
        for j in range(0, i + 1):
            max_sum[i][j] = (triangle[i][j] +
                             max(max_sum[i + 1][j], max_sum[i + 1][j + 1]))

    return max_sum[0][0]


if __name__ == "__main__":
    with open("p067_triangle.txt") as f:
    # with open("problem18.txt") as f:
        triangle = [[int(n) for n in line.split()] for line in f]

    print(max_path_sum(triangle))
