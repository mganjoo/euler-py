# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832. Find the thirteen adjacent digits in the
# 1000-digit number that have the greatest product. What is the value of this
# product?


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


def number_string(resource_accessor):
    with open(resource_accessor.resource_filename("number.txt")) as num_file:
        return "".join(line.strip() for line in num_file)


def test_cases(resource_accessor):
    return [([number_string(resource_accessor), 4], 5832)]


def args(resource_accessor):
    return [number_string(resource_accessor), 13]
