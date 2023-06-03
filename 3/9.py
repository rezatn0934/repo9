lst1 = [("red", "pink"), ("white", "black"), ("orange", "green")]

lst2 = list(map(lambda x: " ".join(x), lst1))
print(lst2)