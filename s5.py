class Student:

    def __init__(self, ID, NAME, AVERAGE):
        self.ID = ID
        self.NAME = NAME
        self.AVERAGE = AVERAGE
    
    def avg(self, other):
        if self.AVERAGE > other.AVERAGE:
            print('True')
        else:
            print('False')
