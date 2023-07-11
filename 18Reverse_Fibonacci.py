r = int(input("Enter Range:- "))
a = int(input("Enter Number A:- "))
b = int(input("Enter Number B:- "))
for i in range(r):
    dif = a - b
    print(dif)
    a = b
    b = dif