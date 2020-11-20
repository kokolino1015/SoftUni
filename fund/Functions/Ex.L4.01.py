n1 = int(input())
n2 = int(input())
n3 = int(input())


def min_number(n1, n2, n3):
    min_numbers = 0
    max_size = 9999999999999
    if n1 < max_size:
        max_size = n1
    if n2 < max_size:
        max_size = n2
    if n3 < max_size:
        max_size = n3
    return max_size


print(min_number(n1, n2, n3))
