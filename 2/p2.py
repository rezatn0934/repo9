try:
    Number = int(input("Enter a number: "))
    Flag = True
except Exception as E:
    # raise ValueError
    print("An error occurred:")
    print(E.__class__.__name__)
    Flag = False
finally:
    if Flag:
        print('\nValid input.')
    else:
        print('\nInvalid input!!!')