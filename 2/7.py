from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def is_valid(passwd):
    if len(passwd) < 8:
        return False
    has_lower = has_upper = has_num = has_punc = False
    for char in passwd:
        print(ch)
        if char >= ascii_lowercase:
            has_lower = True
        elif char >= ascii_uppercase:
            has_upper = True
        elif char >= digits:
            has_num = True
        elif char >= punctuation:
            has_punc = True
    return [has_num, has_punc, has_upper,has_lower]


passw = input()
d = is_valid(passw)

