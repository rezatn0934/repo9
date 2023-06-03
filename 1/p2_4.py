g = float(input('inter your grade: '))
if g < 0 or g > 100:
    print('the input must be in range 0-100!')
elif g <= 25:
    print('F')
elif g <= 45 :
    print('E')
elif g <= 50:
    print('D')
elif g <= 60:
    print('C')
elif g <= 80:
    print('B')
elif 80 < g:
    print('A')