class Student:
    def getStudentInfo(self):
        self._rollno = input("Enter Roll Number: ")
        self._name = input("Enter Name: ")
    def printStudentInfo(self):
        print("Roll Number:", self._rollno)
        print("Name:", self._name)
class Marks(Student):
    def getMarks(self):
        self.getStudentInfo()
        self._marks1 = float(input("Enter marks for subject 1: "))
        self._marks2 = float(input("Enter marks for subject 2: "))
        self._marks3 = float(input("Enter marks for subject 3: "))
    def printMarks(self):
        print("Marks1:", self._marks1)
        print("Marks2:", self._marks2)
        print("Marks3:", self._marks3)
    def calcTotalMarks(self):
        return self._marks1 + self._marks2 + self._marks3
class Result(Marks):
    def getResult(self):
        self.getMarks()
        self._total = self.calcTotalMarks()
    def putResult(self):
        self.printStudentInfo()
        self.printMarks()
        print("Total Marks out of 300:", self._total)
obj = Result()
obj.getResult()
obj.putResult()