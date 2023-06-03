class Student:
    faculty = "Computer"

    def set_faculty(self, faculty):
        self.faculty = faculty


print(Student.faculty)

ali = Student()
print(ali.faculty)
ali.set_faculty("Civil(1)")
print(ali.faculty)


mohamad = Student()
print(mohamad.faculty)
mohamad.set_faculty("Civil(2)")
print(ali.faculty)
