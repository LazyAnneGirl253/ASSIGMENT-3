from grades import Grades
from teacher import Teacher

students = []
teachers = []

def addStudent():
    while True:
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('------------------------------------------------')
        history = input('Grade history: ')
        arts_app = input('Grade arts_app: ')
        oop = input('Grade oop: ')

        stud = Grades(history,arts_app, oop)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def addTeacher():
    while True:
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        type = input('Enter type: ')
        department = input('Enter department: ')
        position = input('Enter position: ')
        subject = input('Enter subject: ')
        print('--------------------------------------')
        teach = Teacher(id, lastName, firstName, type, department, position, subject)
        teach.id = id
        teach.last_name = lastName
        teach.first_name = firstName
        teach.type = type
        teach.deparment = department
        teach.position = position
        teach.subject = subject
        
        teachers.append(teach)
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break
    
    menu()

def deletestudent():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()

def deleteteacher():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()

def searchteacher():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()

def searchstudent():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()

def displaystudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t {students[i].getName()} \t | {students[i].getyear()} \t | {students[i].getcourse()} \t | {students[i].getsection()} \t | {students[i].getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def displayteacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getsubject()} \t | {t.getdepartment()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

print()

def displayall():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t {students[i].getName()} \t | {students[i].getyear()} \t | {students[i].getcourse()} \t | {students[i].getsection()} \t | {students[i].getAverage()}')
        i += 1
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getsubject()} | {t.getdepartment()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def deleteall():
    students.clear()
    teachers.clear()

    menu()

def menu():
    print()
    print()
    print('<<<Menu>>>')
    print('D - delete student          S - delete teacher')
    print('A - add student             W - add teacher')
    print('M - search student          N - search teacher')
    print('G - display student         X - display teacher')
    print('C - display all             Z - delete all')
    print()
    choice = input('Enter a function: ')
    if (choice == 'D'):
        deletestudent()
    elif (choice == 'A'):
        addStudent()
    elif(choice == 'S'):
        deleteteacher()
    elif(choice == 'M'):
        searchstudent()
    elif (choice == 'G'):
        displaystudent()
    elif (choice == 'C'):
        displayall()
    elif(choice == 'W'):
        addTeacher()
    elif(choice == 'N'):
        searchteacher()
    elif(choice == 'X'):
        displayteacher()
    elif(choice == 'Z'):
        deleteall()   
    else:
        print('Invalid choice. Please try again.')
        
    print()

menu()