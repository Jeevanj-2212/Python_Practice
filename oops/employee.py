class Employee:
  def __init__(self,eid,ename,esalary):
     self.eid = eid
     self.ename = ename
     self.esalary = esalary
     self.ecompany = "kodnest"
  def do_job(self,role) :
     print(f"My job role is: {role}")
  def intro(self) :
     print(f"Employee eid: {self.eid}")
     print(f"Employee ename: {self.ename}")
     print(f"Employee esalary: {self.esalary}")
     print(f"Employee ecompany: {self.ecompany}")   
e1 = Employee(101,"rahul",25000)
e1.do_job("developer")
e1.intro()
e2 = Employee(202,"arpit",16000) 
e2.do_job("test Engineer")
e2.intro()
e3 = Employee(303,"raman",20000)
e3.do_job("devOps")
e3.intro()    