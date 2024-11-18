a = int(input("Enter the amount: "))
if(a>=5000):
    print("Discount of 20% is eligible")
    print("Final Price:",(a-(a*20)/100))

elif(a>=3500):
    print("Discount of 15% is eligible")
    print("Final Price:",(a-(a*15)/100))
elif(a>=1500):
        print("Discount of 10% is eligible")
        print("Final Price:",(a-(a*10)/100))
else:
     print("No discount ")   
     print("Final Amount",a)     