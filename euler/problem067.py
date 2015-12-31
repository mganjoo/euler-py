# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with
# one-hundred rows.

import problem018


def solution(triangle):
    return problem018.solution(triangle)


def test_cases(*args):
    return problem018.test_cases(args)


def args(resource_accessor):
    return [problem018.read_triangle(
        resource_accessor.resource_filename("triangle.txt"))]
