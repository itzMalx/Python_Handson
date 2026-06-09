def myFunction(parameter):
    print("Course:",parameter)
    Dept_code=100
import myModule
Course_Name=input("Enter Course Name\n")
print('Course Details:')
myModule.myFunction(Course_Name)
print('Course Code:',myModule.Dept_code)