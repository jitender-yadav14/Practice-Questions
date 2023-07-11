a = int(input("Enter Starting Range:- "))
b = int(input("Enter Ending Range:- "))
c = int(input("Enter Number to Find:-"))
f = 1
for i in range(a,b + 1):
    if(i == c):
        f = 0
        break
if(f == 0):
    print("This Number",i,"is avaialble")
else:
    print("This Number",c,"is out of range")