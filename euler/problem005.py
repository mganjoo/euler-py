# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

import math


def esieve(n):
    isprime = [False, False] + [True] * (n - 1)
    p = 2
    while p * p <= n:
        j = p * p
        while j <= n:
            isprime[j] = False
            j += p

        p += 1
        while p <= n and not isprime[p]:
            p += 1

    return [i for i, x in enumerate(isprime) if x]


def solution(n):
    primes = esieve(n)
    num = 1
    sqrtn = math.sqrt(n)
    for p in primes:
        x = int(math.log(n) / math.log(p)) if p <= sqrtn else 1
        num *= p ** x

    return num


def args():
    return [20]
