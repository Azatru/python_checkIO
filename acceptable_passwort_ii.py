'''In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit.
Input: A string.

Output: A bool.'''
import re


def is_acceptable_password(password):
    return len(password) > 6 and re.search(r'\d+', password) is not None


print(is_acceptable_password("muchlonger"))
