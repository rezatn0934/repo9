from functools import cache


@cache
def fib(num):
    if num <= 1:
        return num
    elif num == 2:
        return 1
    else:
        x = (fib(num-1) + fib(num-2))
        return x


print(fib(400))
