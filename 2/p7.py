def check1(lst, num):
    for number in lst[::2]:
        if num == number:
           return True
    return False
       

try:
    lst = map(int,input().split())
    num = int(input())
    assert check1(lst, num)
    print('Number found in list with even index')
except ValueError:
    print("please write only int!")
except AssertionError:
    print('Number found in list with odd index or not found in list')
    


