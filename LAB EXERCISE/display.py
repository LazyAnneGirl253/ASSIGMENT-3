from student import Student
from teacher import Teacher
from grades import Grades


stu1 = Student
stu1.id = '0245'
stu1.last_name = 'Akagi'
stu1.first_name = 'Aira'
stu1.type = 'Student'
stu1.year = '1'
stu1.course = 'BSCS'
stu1.section = 'A'
print('STUDENT')
print('ID: ' + stu1.id + '\nLast Name: ' + stu1.last_name + '\nFirst Name: ' + stu1.first_name + '\nType: ' + stu1.type + '\nYear: ' + stu1.year + '\nCourse: ' + stu1.course +'\nSection: ' + stu1.section)

stu1 = Grades(78, 89, 90)
print(stu1.getAverage())

print('\n')
print('TEACHER')

teacher1 = Teacher
teacher1.id = '001'
teacher1.last_name = 'Forger'
teacher1.first_name = 'Loid'
teacher1.type = 'Teacher'
teacher1.position = 'Instructor'
teacher1.deparment = 'DCLIS'
teacher1.subject = 'OOP'

print('ID: ' + teacher1.id + '\nLast Name: ' + teacher1.last_name + '\nFirst Name: ' + teacher1.first_name + '\nType: ' + teacher1.type + '\nPosition: ' + teacher1.position + '\nDepartment: ' + teacher1.deparment +'\nSubject: ' + teacher1.subject)

