rows = 5    
columns = 7

for i in range(rows):
    if i == 0 or i == rows - 1:
        
        print("*" * columns)
    else:
        
        print("*" + " " * (columns - 2) + "*")
