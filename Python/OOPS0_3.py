#Online Course
from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def enroll(self):
        pass

class FreeCourse(Course):
    def enroll(self):
        print("Enrolled For Free")
        
class PaidCourse(Course):
    def enroll(self):
        print("Enrolled for Paid")

ins1 = FreeCourse()
ins2 = PaidCourse()
ins1.enroll()
ins2.enroll()