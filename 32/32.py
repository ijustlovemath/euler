import itertools
import math
from collections import deque

def sorted_k_partitions(seq, k):
    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.

    Taken from: https://stackoverflow.com/a/39199937
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    # Sort the parts in each partition in shortlex order
#    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
#    result = sorted(result, key = lambda ps: (*map(len, ps), ps))

    return result

def pandigital_list():
    digits = range(10)
    partitions = list(map(partition_to_tuple, sorted_k_partitions(digits, 3)))
    print("paritions calculated")
    return partitions

def partition_to_tuple(p):
    return tuple(list(map(tuple_to_number, p)))

def tuple_to_number(t):
    return sum(k * 10**i for i, k in enumerate(reversed(t)))

def is_viable(a, b, c):
    return True
    disallowed = {0, 1}
    if a in disallowed or b in disallowed or c in disallowed:
        return False
    if a > c or b > c:
        return False
    return math.log10(c) - .5 <= math.log10(a) + math.log10(b) <= math.log10(c) + .5

def shift(iterable, amount):
    items = deque(iterable)
    items.rotate(amount)
    return tuple(items)

pan_tuples = pandigital_list()

candidates = [p for p in pan_tuples if is_viable(*p)]
candidates.extend([shift(p, 1) for p in pan_tuples if is_viable(*shift(p, 1))])
candidates.extend([shift(p, 2) for p in pan_tuples if is_viable(*shift(p, 2))])
print(len(candidates))
for tup in candidates:
    a, b, c = tup
    if a * b == c or a * c == b or c * b == a:
        print(f"candidate works: {tup}")
