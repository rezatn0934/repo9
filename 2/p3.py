def calculation():
    x = input('>>> ')
    if x != 'quit':
        x = x.split()
        try:
            if len(x) == 3:
                first_num = float(x[0])
                second_num = float(x[2])
                if x[1] == '+' or x[1] == '-':
                    operator = x[1]
                    if operator == '-':
                        result = first_num - second_num
                    elif operator == '+':
                        result = first_num + second_num
                    else:
                        raise ValueError
                    print(result) 
                else:
                    raise ValueError
            else:
                raise ValueError
                    
        except ValueError:
            print('FormulaError!')
        return calculation()
    print('done!')
     
calculation()