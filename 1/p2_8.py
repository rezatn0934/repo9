def select_item(data):
    return data[-1]

sample=[(1,5,3), (5,4,7,2), (4,4)]
# sample.sort(key=lambda a: a[-1])
# print(sample)




sample.sort(key = select_item)
print(sample)