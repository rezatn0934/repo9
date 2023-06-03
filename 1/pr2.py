ages =list(map(float,input().split()))
mini = ages[0]
maxi = ages[0]
for age in ages:
    if age < maxi:
        maxi =age
    if age > mini:
        mini = age
print(mini,maxi)