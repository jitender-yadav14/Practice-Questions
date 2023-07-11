a = int(input("Enter Number to check:- "))
f = 1
for i in range(2,a):
    if(a % i == 0):
        f = 0
        break
if(f == 1):
    print(a,"is Prime Number")
else:
    print(a,"is not Prime Number")
