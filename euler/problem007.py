# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.  What is the 10001st prime number?

import math


def solution(n):
    if n == 1:
        return 2
    i = 2
    p = 3
    while i <= n:
        prime = True
        for j in range(3, int(math.sqrt(p)) + 1, 2):
            if p % j == 0:
                prime = False
                break

        if prime:
            i += 1
        p += 2

    return p - 2


def test_cases(*args):
    return [([6], 13)]


def args(*args):
    return [10001]
