'''You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.'''
from functools import reduce


def checkio(number: int) -> int:
    number = str(number).replace('0', '')
    number = list(map(int, number))
    return reduce(lambda x, y: x*y, number)


print(checkio(123405))
