'''((1) ** 1) / 1,((2)**2) / 2........'''

a = int(input("Enter Number:- "))
result = 0
for i in range(1,a + 1):
    sum = (i / i ) ** i
    result = result + sum
print(result)