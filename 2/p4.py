def capitalize_last_name(s):
    try:
        if not s.replace(" ", "").isalpha():
            raise TypeError
        s = s.split()
        if len(s) != 2:
            raise ValueError
        else:
            a = s[0][0].upper()
            x1 = a + s[0][1:]
            x2 = " " + s[1].upper()
            return x1 + x2
    except ValueError:
        raise ValueError
        
        
    except TypeError:
        raise TypeError
            
        
        
s = input("Enter your name: ")
print(capitalize_last_name(s))

