'''Determine whether the sequence of elements items is ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element.

Input: Iterable with ints.

Output: Bool.'''
from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    if len(set(items)) == 1 and len(items) > 1:
        return False
    return items == sorted(items)


print(is_ascending([-5, 10, 99, 123456]))