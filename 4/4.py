from uuid import uuid4
from random import sample


class Human:
    def __init__(self, first_name, last_name, phone_number, age, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age
        self.email = email


class Student(Human):
    def __init__(self, first_name, last_name, average, phone_number, age, email):
        super().__init__(first_name, last_name, phone_number, age, email)
        self.average = average
        self.std_id = uuid4()


class Teacher(Human):
    def __init__(self, first_name, last_name, phone_number, age, email):
        super().__init__(first_name, last_name, phone_number, age, email)
        self.teacher_id = uuid4()


class Class:
    def __init__(self, class_name, teacher, std_list):
        self.class_name = class_name
        self.teacher_name = teacher.first_name
        self.std_list = std_list
        self.class_id = uuid4()

    def avg(self):
        avg_list = list()
        for std in self.std_list:
            avg_list.append(std.average)
        avg_of_avg = sum(avg_list) / len(avg_list)
        return avg_of_avg

    def best_five(self):
        info_list = list()
        for std in self.std_list:
            std_info = [std.first_name, std.std_id, std.average]
            info_list.append(std_info)
        info_list.sort(key=lambda x: x[-1], reverse=True)
        for std in info_list[:5]:
            print(f"Name: {std[0]}, ID: {std[1]}, Average: {std[2]}")

    def std_number(self):
        return len(self.std_list)


std_list = list()
names_list = ["Amir", "Khorzoo", "Khosro", "Mamad", "Moji", "Neda", "Mahta", "Bita"]
lastname_list = ["AmirZadeh", "KhorzooZadeh", "KhosroZadeh", "MamadZadeh", "MojiZadeh", "NedaZadeh", "MahtaZadeh",
                 "BitaZadeh"]
age_list = list(range(20, 61, 5))
avg_list = sample(range(10, 20), 8)

tchr1 = Teacher("Ahmad", "Alavi", "02134567890", 50, "AA@gamil.com")

for i in range(8):
    obj = Student(names_list[i], lastname_list[i], avg_list[i], None, age_list[i], None)
    std_list.append(obj)

clss1 = Class("Math2", tchr1, std_list)

print(clss1.avg())
clss1.best_five()
print(clss1.std_number())