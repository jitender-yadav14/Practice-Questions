h = int(input("Enter Hindi Marks"))
e = int(input("Enter English Marks"))
m = int(input("Enter Maths Marks"))
sc = int(input("Enter Science Marks"))
sst = int(input("Enter SST Marks"))
total = (h + e + m + sc + sst)
percentage = total / 500 * 100
print(percentage)