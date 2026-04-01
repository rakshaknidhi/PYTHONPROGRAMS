class Employee:
    def __init__(self, name="", age=0, salary=0):
        self.name = name
        self.age = age
        self.salary = salary

    def get_input(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name="", age=0, salary=0, department=""):
        super().__init__(name, age, salary)
        self.department = department

    def get_input(self):
        super().get_input()
        self.department = input("Enter department: ")

    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Process information of 10 managers
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display()
    print("-" * 30)