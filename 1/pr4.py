x = input()
typ = x [-1]
temp = float(x[0:-1])
if typ == 'f' or typ == 'F':
    result = (temp-32)/1.8
    new_type = 'C'
elif typ == 'c' or typ == 'C':
    result = (temp*9/5)+32
    new_type = 'F'
print(result, new_type)