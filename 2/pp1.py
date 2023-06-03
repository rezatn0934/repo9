
# Path = input("Enter Address of file:\n>>>")
Path = 'test.txt'
# with open(Path, 'w') as File:
#     while True:
#         Text = input()
#         if Text:
#             File.write(Text + '\n')
#         else:
#             break
D = []
with open(Path, 'r') as File:
    global Lines
    Lines = File.read()
    print(Lines)
    type(Lines)
    D.append(Lines)
Lines.replace("Global", "reza")