Tuple = eval(input())

if len(Tuple) % 2:
    Tuple = Tuple[:-1]

def create_dict(Tuple):
    dic = dict()
    for i in range(0,len(Tuple),2):
        dic[Tuple[i]] = Tuple[i+1]
    return dic


print(create_dict(Tuple))