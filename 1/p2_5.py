List = input()
if List[0] == '[' or List[-1] == ']':
    List = eval(List)
else:
    List = List.split()        
        
        
counter = 0
for string in List:
    if len(string) > 1 and (string[0] == string[-1]):
        counter += 1
print('Result', counter)
