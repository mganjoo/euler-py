import pkg_resources
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


def args():
    fn = pkg_resources.resource_filename(__name__, "data/p345_matrix2.txt")
    with open(fn) as f:
        rows = [[int(c) for c in row.split()] for row in f]
    return [rows]
