a = int(input("Enter Number A:- "))
b = int(input("Enter Number B:- "))
c = int(input("Enter Number to Find:- "))
for i in range(a,b + 1):
    if(i == c):
        break
print("This Number",i,"is Available")
