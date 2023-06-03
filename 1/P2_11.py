List1 = eval(input())
List2 = eval(input())

def func(List1, List2):
    Lenght = len(List1) if len(List1) < len(List2) else len(List2)
    List = list((List1[i], List2[i]) for i in range(Lenght))
    List.sort(key= lambda x: x[-1], reverse= True)
    return List
print(func(List1, List2))