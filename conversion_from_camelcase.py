'''Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into
the Python format ("my_function_name")
where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.'''
import re


def from_camel_case(name: str) -> str:
    name = re.findall('[A-Z][^A-Z]*', name)
    return '_'.join(name).lower()


print(from_camel_case("MyFunctionName"))
