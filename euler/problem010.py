# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def solution(n):
    isprime = [False, False] + [False, True] * (n - 1)
    p = 2
    sum_primes = 0
    while p <= n:
        sum_primes += p
        j = p * p
        while j <= n:
            isprime[j] = False
            j += p

        p += 1
        while p <= n and not isprime[p]:
            p += 1

    return sum_primes


def full():
    return [2000000]
