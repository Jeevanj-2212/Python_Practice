class Mentor:
    def teach(self):
        print("Mentor teaches")
        
    def __init__(self,name,tech):
        self.name = name
        self.tech = tech
name=input()
tech = input()        
m=Mentor(name,tech)
print(m.name)
print(m.tech)
m.teach()            