from typing import List, Optional


def calculate_average(lst: List[int], ignore_zeros: Optional[bool] = False) -> float:
    if ignore_zeros:
        lst2 = []
        for num in lst:
            if num != 0:
                lst2.append(num)
        return sum(lst2)/len(lst2)
    else:
        return sum(lst)/len(lst)


lst1 = [1, 1, 0, 0]
print(calculate_average(lst1))
print(calculate_average(lst1, ignore_zeros=True))
