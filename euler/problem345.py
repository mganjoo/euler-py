import pkg_resources
from operator import itemgetter
from collections import Counter


def solution(matrix):
    sorted_matrix = [sorted(enumerate(row), key=itemgetter(1), reverse=True)
                     for row in matrix]
    h = len(sorted_matrix)

    idxs = [0] * h
    is_unique_pos = False

    diff = {i: 0 for i in range(h)}
    while not is_unique_pos:
        is_unique_pos = True
        pos = [sorted_matrix[i][j][0] for i, j in enumerate(idxs)]
        counts = Counter(pos)
        next_idx = {}
        for i in range(h):
            if counts[pos[i]] > 1:
                next_idx[i] = idxs[i] + 1
                while (sorted_matrix[i][next_idx[i]][0] in pos):
                    next_idx[i] += 1
                diff[i] = (sorted_matrix[i][idxs[i]][1] -
                           sorted_matrix[i][next_idx[i]][1])
                is_unique_pos = False
            else:
                diff.pop(i, None)
        if not is_unique_pos:
            min_diff = min(diff.values())
            i = min(((i, sorted_matrix[i][idxs[i]][1])
                     for i in range(h) if diff.get(i, -1) == min_diff),
                    key=itemgetter(1))[0]
            idxs[i] = next_idx[i]

    return sum(sorted_matrix[i][j][1] for i, j in enumerate(idxs))


def args():
    fn = pkg_resources.resource_filename(__name__, "data/p345_matrix2.txt")
    with open(fn) as f:
        matrix = [[int(c) for c in row.split()] for row in f]
    return [matrix]
