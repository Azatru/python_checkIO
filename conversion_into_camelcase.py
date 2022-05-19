'''Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name")
into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated
without any intervening characters.

Input: A function name as a string.

Output: The same string, but in CamelCase.'''


def to_camel_case(name: str) -> str:
    name = name.split('_')
    name = [word.capitalize() for word in name]
    return ''.join(name)


print(to_camel_case('my_function_name'))