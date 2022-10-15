def valid_anagram(s: str, t: str):
    return sorted(s) == sorted(t)
