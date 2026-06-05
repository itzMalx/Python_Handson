class Person:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)


class Trainee(Person):

    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications):
        super().__init__(name, age, email)
        self.batch_id = batch_id
        self.marks = marks
        self.num_projects = num_projects
        self.num_publications = num_publications

    def display_info(self):
        super().display_info()
        print("Batch:", self.batch_id)
        print("Marks:", self.marks)
        print("Projects:", self.num_projects)
        print("Publications:", self.num_publications)

class SDETTrainee(Trainee):

    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications, tool):
        super().__init__(name, age, email, batch_id, marks, num_projects, num_publications)
        self.tool = tool

    def compute_aggregate(self):
        avg = sum(self.marks) / len(self.marks)
        return (avg * 0.6) + (self.num_projects * 5) + (self.num_publications * 3)

    def display_info(self):
        super().display_info()
        print("Tool:", self.tool)

t1 = SDETTrainee("Arun", 24, "arun@gmail.com", "B2025", [78,85,90,72,88], 3, 1, "Selenium")
t2 = SDETTrainee("Vijay", 23, "vijay@gmail.com", "B2025", [90,92,95,89,91], 4, 2, "Playwright")
trainees = [t1, t2]

highest = trainees[0]

for t in trainees:
    t.display_info()
    print("Aggregate:", t.compute_aggregate())

    if t.compute_aggregate() > highest.compute_aggregate():
        highest = t

print("Highest Aggregate:", highest.name)
 