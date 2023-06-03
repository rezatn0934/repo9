def show_employee(name, salary = 9000):
    print('name: ', name,'salary: ',salary)
    
    
n = input("Enter ypur name: ")
s = input("Enter your salary: ")

if s != "":
    show_employee(n,s)
else:
    show_employee(n)