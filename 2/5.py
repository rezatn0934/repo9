from functools import reduce


lst = list(map(int, input().split()))


# mult = 1
# for num in lst:
#     mult *= num
mult = reduce(lambda x,y: x*y , lst)


if __name__=="__main__":
    print(mult)