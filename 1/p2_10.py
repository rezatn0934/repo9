import string

alphabet = set(string.ascii_lowercase)

input_string = 'the quick brown fox jumps over the lazy dog *& #'
print(set(input_string.lower()) >= alphabet)


