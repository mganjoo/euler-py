# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits in the
# 1000-digit number that have the greatest product. What is the value of this
# product?

import pkg_resources


def solution(n_str, count):
    n = len(n_str)
    prod = 1
    max_prod = prod
    no_max_till = 0

    for i in range(n):
        if n_str[i] == "0":
            no_max_till = i + count
        prv = max(int(n_str[i - count]), 1) if i >= count else 1
        nxt = max(int(n_str[i]), 1)
        prod = prod // prv * nxt
        if i >= no_max_till and prod > max_prod:
            max_prod = prod

    return max_prod


def args():
    fn = pkg_resources.resource_filename(__name__, "data/p008_number.txt")
    with open(fn) as num_file:
        num_str = "".join(line.strip() for line in num_file)
    return [num_str, 13]
