'''Our robots are always working to improve their linguistic skills. For this mission, t
hey research the Latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by whitespaces and punctuation marks.
Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).
You should count the number of words (striped words) where the vowels with consonants are alternating;
words that you count cannot have two consecutive vowels or consonants.
The words consisting of a single letter are not striped -- don't count those.
Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.'''


def checkio(line: str) -> int:
    vowels = set('aeiouy')
    consonants = set('bcdfghjklmnpqrstvwxz')
    line = ''.join(ch if ch.isalnum() else ' ' for ch in line).lower().split()
    line = [word for word in line if word.isalpha() and len(word) > 1]
    counter = 0
    for word in line:
        if (not set(word[1::2]) - vowels and not set(word[::2]) - consonants) \
                or (not set(word[::2]) - vowels and not set(word[1::2]) - consonants):
            counter += 1
    return counter


print(checkio('1st 2a ab3er root rate'))
