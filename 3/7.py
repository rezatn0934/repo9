def get_list(R):
    List = list()
    while R:
        Name = input("Name: ")
        Grade = float(input("Grade: "))
        List.append([Name, Grade])
        R -= 1
    return List


number = int(input("Number of students:\n>>> "))
list_of_list= get_list(number)
print(f"\nNames and Grades of all students:\n{list_of_list}")
set_of_grades = list(set(map(lambda x: x[1], list_of_list)))



for i in list_of_list:
    if i[1] == set_of_grades[1]:
        target = i
    print(f"\nSecond lowest Grade of all students:\n{target[0]}\nGrade: {target[1]}")

