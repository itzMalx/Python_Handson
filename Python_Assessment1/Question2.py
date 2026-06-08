class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def display_info(self):
        print("Name: ", self.name, " | ", "Age: ", self.age)

class Trainee(Person):

    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications):
        super().__init__(name, age, email)
        self.batch_id = batch_id
        self.marks = marks
        self.num_projects = num_projects
        self.num_publications = num_publications
    
    def display_info(self):
        super().display_info()
        print("Batch ID: ", self.batch_id)
        print("Marks: ", self.marks, " | ", "Avg: ", sum(self.marks)/len(self.marks))
        print("Projects: ", self.num_projects, " | " , "Publications: ", self.num_publications)

class SDETTrainee(Trainee):
    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications, tool_proficiency):
        super().__init__(name, age, email, batch_id, marks, num_projects, num_publications)
        self.tool_proficiency = tool_proficiency

    def compute_aggregate(self):
        agg = (sum(self.marks)/len(self.marks)) * 0.6
        proj = (self.num_projects * 5)
        pub = (self.num_publications * 3)

        return agg + proj + pub

    def display_info(self):
        super().display_info()
        print("Tool: ", self.tool_proficiency)
        print("Aggregate Score: ", self.compute_aggregate())

obj1 = SDETTrainee("Arun", 45, "arun@gmail.com", "B2025", [78, 85, 90, 72, 88],3,1,"Selenium")
obj1.display_info()