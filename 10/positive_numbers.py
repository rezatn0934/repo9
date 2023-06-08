from typing import List, Iterator


def get_positive_numbers(lst: List[int]) -> Iterator[int]:
    for num in lst:
        if num > 0:
            yield num


lst = [-1, 2, -3, 4]
lst2 = get_positive_numbers(lst)
print(list(lst2))
