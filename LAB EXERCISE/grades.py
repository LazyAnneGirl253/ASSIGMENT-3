from student import Student

class Grades(Student):
    def __init__(self, history, arts_app, oop):
     self.history = history
     self.arts_app = arts_app
     self.oop = oop

    
    def getAverage(self):
        return (int(self.history) + int(self.arts_app) + int(self.oop))/3
