from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
        
    def list_students(self):
        number = 1
        for student in self.students:
            print(f"{number}. {student.name} {student.school_id}")
            number += 1
        
            
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
        return 'No student by that id found.'
        
            
