def factorial_1(x):
    r=1
    if x == 0 or x == 1:
        return r
    else:
        for i in range(1,x+1):
            r = r*i
        return r
        
 
x = int(input())
for i in range(x+1):
    for j in range(i+1):        
        print(factorial_1(i)//(factorial_1(j)*factorial_1(i-j)), end=" ")     
    print()