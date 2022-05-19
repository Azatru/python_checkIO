'''You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = " H ow are you? E h, ok. L ow or L ower? O hhh.",
if we collect all of the capital letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.'''


def find_message(message: str) -> str:
    return ''.join(ch for ch in message if ch.isalpha() and not ch.islower())


print(find_message(('HELLO WORLD!!!')))
