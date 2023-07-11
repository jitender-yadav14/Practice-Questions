a = float(input("Enter No: "))
b = float(input("Enter No: "))
c = float(input("Enter No: "))

if(a > c and a > b ):
    print("A is greater")
elif(b > c and b > a):
    print("B is greater")
elif(c > a and c > b):
    print("C is Greater")
else:
    print("All are same")