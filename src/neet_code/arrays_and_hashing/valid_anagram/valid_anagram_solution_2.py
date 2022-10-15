from collections import defaultdict
from email.policy import default


from typing import Dict


def count_chars(text: str) -> Dict[str, int]:

    res = {}
    for c in text:

        if c in res:
            res[c] += 1
        else:
            res[c] = 1

    return res


def valid_anagram(s: str, t: str):

    return count_chars(s) == count_chars(t)
