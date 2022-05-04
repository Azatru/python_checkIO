from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    return sum([(odd - even).total_seconds() for odd, even in zip(els[1::2], els[::2])])


print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 11, 10, 10),
    datetime(2015, 1, 12, 12, 10, 10),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 1),
]))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 13, 11, 0, 0),
]))


