'''Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.

Output: a boolean.
Precondition: a-z, A-Z, 1-9 and spaces'''


def is_all_upper(text: str) -> bool:
    # your code here
    return text.isupper()


print(is_all_upper(""))