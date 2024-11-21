class Parent:
    def __init__(self,name):
        print("Parent constructor")
        self.name = name
        
    def fun(self):
        print("Parent fun")

class Child(Parent):
    def fun(self):
        print("Child fun")
        super().fun()  
    def intro(self):
        print(f"Name: {self.name}")    
name = input()

c = Child(name)
c.fun()
c.intro()
