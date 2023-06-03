import operator as op


def Calculate(Number1, Operator, Number2):
    if Operator == '+':
        return op.add(Number1, Number2)
    elif Operator == '-':
        return op.sub(Number1, Number2)
    elif Operator == '*':
        return op.mul(Number1, Number2)
    elif Operator == '/':
        return op.mul(Number1, (1 / Number2))
    else:
        raise TypeError
        
        
def Calculator():
    try:
        List= input("\nEnter Formula:\n>>> ").split()
        if List[0] == 'quit':
            print('Done')
            quit()
        Number2 = float(List[2])
        print(Number2)
        Number1 = float(List[0])
        Operator = List[1]
        Result = Calculate(Number1, Operator, Number2)
        print("Result:\n>>>",Result)
    except ValueError:
        print("Formula Error: Numbers are not int or float!!!")
    except TypeError:
        print("Formula Error: Operator is not valid!!!")
    except IndexError:
        print("Formula Error: 3 value needed!!!")
        
        
while True:
    Calculator()

