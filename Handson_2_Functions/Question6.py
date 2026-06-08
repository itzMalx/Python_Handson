oldSalary = float(input("Enter the salary : "))
rating = float(input("Enter the rating : "))

def salaryHike(salary, hike):
    return salary + (salary * hike / 100)

if 1 <= rating <= 4:
    newSalary = salaryHike(oldSalary, 10)

elif 4 < rating <= 7:
    newSalary = salaryHike(oldSalary, 25)

elif 7 < rating <= 10:
    newSalary = salaryHike(oldSalary, 30)

else:
    print("Invalid input")
    exit()

print("Salary after hike is", newSalary)