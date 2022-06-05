from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, employee_id, name, password, age, role):
        self.employee_id = employee_id
        super().__init__(name, password, age, role)
        
    def all_staff():
        staff = []
        with open('data/staff.csv', newline='') as f:
            staff_reader = csv.reader(f, delimiter=' ')
            next(staff_reader)
            for row in staff_reader:
                staff.append(''.join(row))
        return staff