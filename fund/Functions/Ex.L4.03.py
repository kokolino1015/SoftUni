n1 = input()
n2 = input()


def solve():
    f = []
    g = ord(n1) + 1
    g2 = ord(n2)
    for h in range(g, g2):
        f.append(chr(h))
    return ' '.join(f)


print(solve())
