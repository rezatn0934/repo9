Number = int(input(">>> "))


Total = 0
print('Divisors: ')
for i in range(1, Number // 2 + 2):
    if not Number % i:
        print (i, end= ' ')
        Total += i
print('=',Total, '\n-----\nAnswer:')
print('YES' if Number == Total else 'NO')