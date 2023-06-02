from cal import calculator

def Calculator():
    List= input(">>> ").split()
    try:
        if List[0] == 'exit':
            print('Done')
            return False
        else:
            Number2 = float(List[2])
            Number1 = float(List[0])
            Operator = List[1]
            Result = calculator(Number1, Operator, Number2)
            print("Result: ",Result)
            return [Number1,Operator, Number2,Result]
    except ValueError:
        print("Invalid Number Exception!")
    except TypeError:
        print("Invalid Operator Exception!")
    except IndexError:
        print("Invalid Format Exception!")

while True:
    Calculator()