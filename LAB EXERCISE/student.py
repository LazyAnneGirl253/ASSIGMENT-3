from person import Person

class Student(Person):

    def __init__(self, id, last_name, first_name, type, year, course, section):
        Person.__init__(self, id, last_name, first_name, type)
        self.year = year
        self.course = course
        self.section = section

    def getyear(self):
        return self.year

    def getcourse(self):
        return self.course

    def getsection(self):
        return self.section
