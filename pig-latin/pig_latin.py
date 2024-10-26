def translate(text):
    phrase = ""
    for word in text.split(" "):
        phrase += translate_word(word) + " "
    return phrase.strip()

def translate_word(word):
    if word[0].lower() in ['a','e','i','o','u'] or (len(word) >=2 and word[:2] in ('xr', 'yt')):
        return word + 'ay'
    if len(word) >=2 and word[:2].lower() == 'qu':
        return word[2:] + 'quay'
    first = first_vowel(word)
    if first == None:
        raise ValueError("no vowels")
    if first == 0 and word[0].lower() == 'y':
        return word[1:] + 'yay'
    if word[first] == 'u' and word[first-1] == 'q':
        return word[first+1:] + word[:first+1] + 'ay'
    return word[first:] + word[:first] + 'ay'

def first_vowel(word):
    first_vowel = None
    for vowel in ['a', 'e', 'i', 'o', 'u', 'y']:
        try:
            index = word.lower().index(vowel)
            if first_vowel is None or index<first_vowel:
                first_vowel = index
        except:
            continue
    return first_vowel
