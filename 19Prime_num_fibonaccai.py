a = int(input("Enter Number:- "))
n1 = 0
n2 = 1
for i in range(a):
    f = 1
    sum = n1 + n2
    n1 = n2 
    n2 = sum
    for j in range(2,a):
        if (sum % 2 == 0):
            f = 0
            break
    if (f == 1):
        print("This",sum,"is prime")