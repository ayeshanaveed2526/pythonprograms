class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
Ayesha = Student("Ayesha", 20, "A")
Ayesha.display_student()

