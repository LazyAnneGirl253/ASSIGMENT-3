from person import Person

class Teacher(Person):
    def __init__(self, id, last_name, first_name, type, department, position, subject):
        Person.__init__(id, last_name, first_name, type)

        self.deparment = department
        self.position = position
        self.subject = subject

    def getdepartment(self):
          return self.deparment
    def getposition(self):
          return self.position
    def getsubject(self):
         return self.subject
    