# Parent Class
class BasicInfo:
    def __init__(self):
        self.name = input("What is your name? ")
        self.age = int(input("What is your age? "))
        self.contact = input("What is your contact number? ")
        self.city = input("What city do you live in? ")
        self.country = input("What country do you live in? ")

    # Method for displaying info
    def display_info(self):
        print("\n--- Basic Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Contact: {self.contact}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")


# Child Class (Inheritance)
class ExtraInfo(BasicInfo):
    def __init__(self):
        # Call Parent Constructor
        super().__init__()

        self.degree = input("What is your degree? ")
        self.hobby = input("What is your hobby? ")
        self.siblings = int(input("How many siblings do you have? "))
        self.friendname = input("What is your best friend's name? ")
        self.activecourse = input("What is your active course? ")
        self.favlanguage = input("What is your favorite programming language? ")
        self.strength = input("What is your strength? ")
        self.weakness = input("What is your weakness? ")
        self.business = input("What is your business? ")
        self.favoritefood = input("What is your favorite food? ")
        self.favsubject = input("What is your favorite subject? ")
        self.career = input("What is your career? ")
        self.gpa = float(input("What is your GPA? "))
        self.futureplan = input("What is your future plan? ")
        self.religion = input("What is your religion? ")

    # Polymorphism (Method Overriding)
    def display_info(self):
        # Call parent method first
        super().display_info()

        print("\n--- Extra Information ---")
        print(f"Degree: {self.degree}")
        print(f"Hobby: {self.hobby}")
        print(f"Siblings: {self.siblings}")
        print(f"Best Friend's Name: {self.friendname}")
        print(f"Active Course: {self.activecourse}")
        print(f"Favorite Programming Language: {self.favlanguage}")
        print(f"Strength: {self.strength}")
        print(f"Weakness: {self.weakness}")
        print(f"Business: {self.business}")
        print(f"Favorite Food: {self.favoritefood}")
        print(f"Favorite Subject: {self.favsubject}")
        print(f"Career: {self.career}")
        print(f"GPA: {self.gpa}")
        print(f"Future Plan: {self.futureplan}")
        print(f"Religion: {self.religion}")


# Creating Object
person = ExtraInfo()

# Polymorphism in action
person.display_info()