from classes.student import Student
from classes.staff import Staff
from csv import writer
import pandas as pd

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
        
    def add_student(self, name, age, school_id, password, role):
        new_student_info = [name,age,role,school_id,password] #creating list to pass into csv file from student data object
        with open('data/students.csv', 'a', newline='') as f: #opening csv file and appending 
            writer_obj = writer(f)
            writer_obj.writerow(new_student_info) #passing info into student.csv
            f.close() 
        self.students.append(Student(school_id, name, password, age, role)) #appending new student info self.students list of objects
        
    def remove_student(self, student_id):
        df = pd.read_csv('data/students.csv')
        df = df[df['school_id'] != int(student_id)] # df.column_name != whole string from the cell
        df.to_csv('data/students.csv', index=False)# now, all the rows with the column: Name and Value: "dog" will be deleted
        self.students = Student.all_students()