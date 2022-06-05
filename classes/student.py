from classes.person import Person
import csv
class Student(Person):
    def __init__(self, school_id, name, password, age, role):
        self.school_id = school_id
        # print(self.school_id)
        super().__init__(name=name, password=password, age=age, role=role)
        
    def __str__(self):
        return f'Name: {self.name}\tID: {self.school_id}\tRole: {self.role}\tPassword: {self.password}\tAge: {self.age}'
    
    
    def all_students():
        student_objects = []
        with open('data/students.csv', newline='') as f:
            student_reader = csv.reader(f, delimiter=' ')
            next(f)
            for row in student_reader:
                items = row[0].split(',')
                student_info = {'name' : items[0], 'password' : items[4], 'school_id' : items[3], 'age' : items[1], 'role' : items[2]}
                student_objects.append(Student(**student_info))
        f.close()
        return student_objects
    