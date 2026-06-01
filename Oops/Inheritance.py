class TeamMember:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
    def display(self):
        print(f"TeamMember: {self.name} UID: {self.uid}")
class Worker:
    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle
    def display(self):
        print(f"Worker: {self.jobtitle}, Pay: {self.pay}")
obj1 = TeamMember("Jake", 101)
obj1.display()
obj2 = Worker(50000, "Tester")
obj2.display()