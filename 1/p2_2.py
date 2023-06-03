numbers = list(map(int,input().split()))
x = []
for num in numbers:
    if num %2 == 0:
        x.append(num)
print(x)