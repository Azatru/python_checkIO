'''In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain at least 3 different letters (or digits) even if it is longer than 10.'''
import re


def is_acceptable_password(password):
    if ('password' in password.lower()) or len(set(password)) < 3:
        return False
    return (6 < len(password) <= 9 and bool(re.search(r'\d+', password) and not password.isdigit())) \
           or len(password) > 9


print(is_acceptable_password("aaaaaa1"))
