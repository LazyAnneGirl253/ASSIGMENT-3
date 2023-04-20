from teacher import Teacher

class Load(Teacher):
    def __init__(self, id, last_name, first_name, department, position, load):
        Teacher.__init__(id, last_name, first_name, department, position)
        self.load = load

    def add_load(self, subject, section):
        return (subject, section)
    
    def get_load(self):
        return self.load

