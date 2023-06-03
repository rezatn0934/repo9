
List = eval(input(">>> ").lower)

Pointer = len(List) // 3


if (len(List) % 3):
    Pointer += 1
    
    

for i in range(0,len(List),Pointer):
    Short_List = List[i : i+pointer]
    New_List.append(Short_List)
    New_List.append(Short_List[::-1])
for L in New_List:
    print(L)
