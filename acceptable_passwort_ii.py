'''In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit.
Input: A string.

Output: A bool.'''
import re


def is_acceptable_password(password):
    if 'password' in password.lower():
        return False
    return (6 < len(password) <= 9 and bool(re.search(r'\d+', password) and not password.isdigit())) \
           or len(password) > 9


print(is_acceptable_password("PASSWORD12345"))
