# The largest integer <= 100 that is only divisible by both the primes 2 and 3
# is 96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N) be the
# largest positive integer <=N only divisible by both p and q and M(p,q,N)=0 if
# such a positive integer does not exist.

# E.g. M(2,3,100)=96.  M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3
# and 5.  Also M(2,73,100)=0 because there does not exist a positive integer <=
# 100 that is divisible by both 2 and 73.

# Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

# Find S(10 000 000).


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


def divides_out(n, p, q):
    while n % p == 0:
        n //= p

    while n % q == 0:
        n //= q

    return n == 1


def solution(n):
    primes = esieve(n)
    s = set()
    for ii in range(len(primes) - 1):
        for jj in range(ii + 1, len(primes)):
            i = primes[ii]
            j = primes[jj]
            if i * j > n:
                break
            for k in range(n - (n % (i * j)), 1, -(i * j)):
                if divides_out(k, i, j):
                    s.add(k)
                    break

    return sum(s)


def test_cases(*args):
    return [([100], 2262)]


def args(*args):
    return [10000000]
