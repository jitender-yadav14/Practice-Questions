'''(1) + (1 + 2) + (1 + 2 + 3)......'''
a = int(input("Enter the Number:-" ))
b = 0
for i in range(a + 1):
    for j in range(i + 1):
        b = j + b
print(b)
