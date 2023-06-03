numbers = list(map(int,input().split()))
even_cunt =[]
odd_cunt = []
for num in numbers:
    if num %2 == 0:
        even_cunt.append(num)
    else:
        odd_cunt.append(num)
print(len(even_cunt))
print(len(odd_cunt))