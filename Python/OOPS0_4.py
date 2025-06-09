class Student:
    def __init__(self, marks):
        self.__marks = marks
    
    def set_marks(self, marks):
        self.__marks = marks
        print(self.__marks)
    
    def get_marks(self):
        print(self.__marks)

tarun = Student(97)
# print(tarun.__marks)
tarun.get_marks()