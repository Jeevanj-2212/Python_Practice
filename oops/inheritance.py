class Employee:
    def __init__(self,eid,ename,esalary,ecompany):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
        self.ecompany = ecompany
    def intro (self):
        print(f"Name: {self.ename} Salary: {self.esalary}")
    def software_skills(self):
        print("Good ") 
    def coding(self):
        print("Good coding skills") 

class Developer(Employee):
    def coding(self):
        print("excellent")
      
class Tester(Employee):
    def debugging(self):
        print("Excellent debugging skills")            
t = Tester("abc","rama","80000","xyz")
t.intro()
t.software_skills()
t.debugging()
d = Developer("def","ramesha","45000","wer")
d.intro()
