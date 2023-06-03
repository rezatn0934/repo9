from collections import Counter

while True:
    s=input(">>>")
    if not s:
        break
    else:
        with open(s,"r") as i :
            ahmad = i.read()
        with open('output1.txt',"a") as d:
            d.write(ahmad+ " ")
            
with open("output1.txt", 'r') as f:
    c = Counter(word.strip() for word in f.read().split())
    print(c.most_common(6))