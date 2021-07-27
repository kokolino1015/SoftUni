from itertools import permutations


def possible_permutations(seq):
    return (list(p) for p in permutations(seq))
