# We define the Matrix Sum of a matrix as the maximum sum of matrix elements
# with each element being the only one in his row and column. For example, the
# Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

#   7  53 183 439 863
# 497 383 563  79 973
# 287  63 343 169 583
# 627 343 773 959 943
# 767 473 103 699 303

from operator import itemgetter
from collections import Counter


def solution(rows):
    sorted_rows = [sorted(enumerate(row), key=itemgetter(1), reverse=True)
                   for row in rows]
    h = len(sorted_rows)

    idxs = [0] * h
    has_dupes = True

    diff = {i: 0 for i in range(h)}
    while has_dupes:
        has_dupes = False
        pos = [sorted_rows[i][j][0] for i, j in enumerate(idxs)]
        counts = Counter(pos)
        next_idx = {}
        for i in range(h):
            if counts[pos[i]] > 1:
                next_idx[i] = idxs[i] + 1
                while (sorted_rows[i][next_idx[i]][0] in pos):
                    next_idx[i] += 1

                diff[i] = (sorted_rows[i][idxs[i]][1] -
                           sorted_rows[i][next_idx[i]][1])
                has_dupes = True
            else:
                diff.pop(i, None)

        if has_dupes:
            # Move index on row with minimum difference from next (and minimum
            # current value in case of ties)
            change_i = min(diff,
                           key=lambda i: (diff[i], sorted_rows[i][idxs[i]][1]))
            idxs[change_i] = next_idx[change_i]

    return sum(sorted_rows[i][j][1] for i, j in enumerate(idxs))


def read_matrix(filename):
    with open(filename) as f:
        return [[int(c) for c in row.split()] for row in f]


def test_cases(resource_accessor):
    return [([read_matrix(resource_accessor.resource_filename("matrix1.txt"))],
             3315)]


def args(resource_accessor):
    return [read_matrix(resource_accessor.resource_filename("matrix2.txt"))]
