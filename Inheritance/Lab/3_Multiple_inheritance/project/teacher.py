from project.employee import Employee
from project.person import Person

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

t = Teacher()
print(t.teach())
print(t.get_fired())
print(t.sleep())