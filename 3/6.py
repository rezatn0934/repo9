def Get_List(String):
    List = input(f"List of {String}:\n>>> ").strip("[]").split(',')
    return List


def Merge(List1, List2):
    Lenght = len(List1) if len(List1) <= len(List2) else len(List2)
    Main_List = list()
    for i in range(Lenght):
        Main_List.append((List1[i].replace("'", '').replace('"', '').strip(), int(List2[i])))
    return Main_List



def Sort(List : list):
    List.sort(key= lambda x: (x[0], x[1]))
    return List


List1 = Get_List('Names')
List2 = Get_List('Ages')
Main_List = Merge(List1, List2)
print(f"Result:\n{Sort(Main_List)}")

