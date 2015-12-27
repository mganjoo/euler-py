def find_largest_product_window(n_str, count):
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
            l = i - count + 1
            r = i + 1
            max_prod = prod

    return (l, r, max_prod)


def print_find_largest_product_window(n_str, count):
    l, r, max_prod = find_largest_product_window(n_str, count)
    print("Largest {}-digit product in number is {} = {}".format(
        count, "x".join(n_str[l:r]), max_prod
    ))


if __name__ == "__main__":
    with open("problem8.txt") as num_file:
        num_str = "".join(line.strip() for line in num_file)

    print_find_largest_product_window(num_str, 4)
    print_find_largest_product_window(num_str, 13)
