# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

import math


def esieve(n):
    isprime = [False, False] + [False, True] * (n - 1)
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


def smallest_multiple_seq(n):
    primes = esieve(n)
    num = 1
    sqrtn = math.sqrt(n)
    for p in primes:
        x = int(math.log(n) / math.log(p)) if p <= sqrtn else 1
        num *= p ** x

    return num


def print_smallest_multiple_seq(n):
    print("Smallest number divisible by all numbers from 1 to {} is {}"
          .format(n, smallest_multiple_seq(n)))

if __name__ == "__main__":
    print_smallest_multiple_seq(10)
    print_smallest_multiple_seq(20)
    print_smallest_multiple_seq(30)
