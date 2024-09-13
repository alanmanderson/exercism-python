def is_isogram(string):
    string = string.replace(" ", "").replace("-", "").lower()
    arr = [c for c in string]
    s = set(arr)
    return len(arr) == len(s)
