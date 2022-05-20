'''You are given a list of files. You need to sort this list by the file extension.
The files with the same extension should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".
Input: A list of filenames.

Output: A list of filenames.'''
from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    files.sort(key=lambda x: (x if '.' == x[0] and '.' not in x[1:] else x.split('.')[-1], x.split('.')[:-1]))
    if '.config' in files:
        files.insert(0, files.pop(files.index('.config')))
    return files


print(sort_by_ext(["1.cad","1.bat","1.aa",".bat"]))