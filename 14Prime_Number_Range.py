sr = int(input("Enter Starting Range:- "))
er = int(input("Enter Ending Range:- "))
for i in range(sr,er):
    f = 1
    for j in range(2,i):
        if(i % j == 0):
            f = 0
            break
    if(f == 1):
        print("This Number",i,"is Prime")