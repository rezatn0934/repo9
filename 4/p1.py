class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary


teacher1 = Teacher(name="ahmad", age=35, salary=2000)
print(teacher1._Teacher__salary)
