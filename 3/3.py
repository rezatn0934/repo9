

def Convert_to_Dict(List):
    Dict = dict()
    for i in List:
        k,v = i.split(':')
        Dict[k] = int(v)
    return Dict


List = (input("Enter dictionary:\n>>> ")).strip("{}").split(',')
Dict = Convert_to_Dict(List)
print(f"\nResult:\n{list(set(Dict.values()))}")