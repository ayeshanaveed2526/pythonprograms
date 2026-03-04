class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        total_salary = self.salary + self.bonus
        print(f"Total Salary for Manager {self.name}: ${total_salary}")
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_language(self):
        print(f"{self.name} is proficient in {self.programming_language}.")
class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def show_tool(self):
        print(f"{self.name} uses {self.design_tool} for designing.")
manager = Manager("Alice", 80000, 15000)
developer = Developer("Bob", 70000, "Python")
designer = Designer("Charlie", 60000, "Adobe Photoshop")
manager.display_info()
manager.calculate_total_salary()
developer.display_info()
developer.show_language()
designer.display_info()
designer.show_tool()

