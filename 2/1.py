import random

start, end, length = map(int,input().split())

sequence = range(start, end + 1)
lst = (random.sample(sequence, length))

print(lst)