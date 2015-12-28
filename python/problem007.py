import math


def nth_prime(n):
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


def print_nth_prime(n):
    print("Prime #{} = {}".format(n, nth_prime(n)))


if __name__ == "__main__":
    print_nth_prime(10001)
