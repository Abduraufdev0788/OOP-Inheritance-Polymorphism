class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return "Bonus hisoblash har bir rolda farq qiladi."

class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.10  # 10% bonus
        return f"{self.name} (Developer) bonusi: {bonus}"


class Manager(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.20  # 20% bonus
        return f"{self.name} (Manager) bonusi: {bonus}"


dev = Developer("Ali", 8000)
mgr = Manager("Vali", 10000)

print(dev.calculate_bonus())
print(mgr.calculate_bonus())
