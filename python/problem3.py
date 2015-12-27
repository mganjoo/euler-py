# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def largest_prime_factor(n):
    if n == 1:
        return 1
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 2
    p = 3
    maxp = math.sqrt(n)
    while n > 1 and p <= maxp:
        if n % p == 0:
            while n % p == 0:
                n //= p

            maxp = math.sqrt(n)

        if n > 1:
            p += 2

    return p if n == 1 else n


def print_largest_prime_factor(n):
    print("Largest prime factor of {} is {}"
          .format(n, largest_prime_factor(n)))

if __name__ == "__main__":
    print_largest_prime_factor(13195)
    print_largest_prime_factor(600851475143)
    print_largest_prime_factor(9007199254740991)
    print_largest_prime_factor(9007199254740993)
