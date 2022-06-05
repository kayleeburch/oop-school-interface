from classes.school import School 
from classes.person import Person
from classes.student import Student
from classes.staff import Staff

def main():
    ridge = School('Ridgemont High') 
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    if mode == '1':
        ridge.list_students()
        main()
    elif mode == '2':
        student_id = input('Enter student id:')
        found_student = ridge.find_student_by_id(student_id)
        if isinstance(found_student, str):
            print(found_student)
            main()
        else:
            print(str(found_student))
            main()
    elif mode == '3':
        main()
    elif mode == '4':
        main() 
    elif mode == '5':
        return
    else:
        print('Incorrect entry, please try again.')
        main()
        
if __name__ == '__main__':
    main()