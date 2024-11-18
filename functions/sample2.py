#Without Parameter
def add():
    a = 22
    b = 30
    print("Sum",(a+b))
add()  
#without parameter and with return type 
def add1():
    a = 22
    b = 39
    res = a+b
    return res

print("Sum",add1());  
#With parameter and return type
def add2(a,b):
    
    res = a+b
    return res

print("Sum",add2(10,20))
# Parameter but no return value
def add3(a,b):
    
    res = a+b
    print("Sum",res)
add3(20,30)
