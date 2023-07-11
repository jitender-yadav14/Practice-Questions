a = int(input("Enter Number:- "))
n1 = 0
n2 = 1
for i in range(a):
    sum = n1 + n2
    print(sum)
    n1 = n2
    n2 = sum 

    