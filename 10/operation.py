from typing import Callable
import operator as op


def perform_operation(num1: int, num2: int, operator: Callable[[int, int], int]) -> int:
    return operator(num1, num2)


print(perform_operation(num1=2, num2=3, operator=op.mul))
