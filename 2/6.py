

def sum1(num=10):
    if num == 1:
        return 1
    return num + sum1(num-1)


print(sum1(3))