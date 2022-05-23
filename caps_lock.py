'''Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends
to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes
to conjure the accents, he is more careful in the presence of such raffinated characters ([Shift] + [Char])
and will press the keys correctly.) Compute and return the result of having Joe type in the given text.
The “Caps Lock” key affects only the letter keys from “a” to “z” , and has no effect on the other keys or characters.
“Caps Lock” key is assumed to be initially off.

For Joe's keyboard, Caps Lock is always uppercase a letter.
That means if Caps Lock is on, and Joe does Shift + b - he gets 'B' (in upper case) printed.

Input: A string. The typed text.

Output: A string. The showed text after being typed.'''


def caps_lock(text: str) -> str:
    caps_lock = False
    new_text = ''
    for ch in text:
        if ch == 'a' or ch == 'z':
            caps_lock = not caps_lock
            continue
        elif caps_lock and ch.islower():
            ch = ch.upper()
        new_text += ch

    return new_text


print(caps_lock("Always wanted to visit Zambia."))


# def caps_lock(text: str) -> str:
#     return ''.join(c.upper() if i % 2 else c for i, c in enumerate(text.split('a')))



# def caps_lock(text: str) -> str:
#     parts = text.split('a')
#     for i in range(1, len(parts), 2):
#         parts[i] = parts[i].upper()
#     return ''.join(parts)
