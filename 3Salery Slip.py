bs = int(input("Enter Basic Salary:-"))
pf = int(input("Enter PF:-"))
pf1 = bs * pf / 100
hra = int(input("Enter HRA:-"))
hra1 = bs * hra / 100
esi = int(input("Enter ESI:-"))
esi1 = bs * esi / 100
sa = int(input("Enter SA:-"))
sa1 = bs * sa / 100
gross_salary = (bs + pf1 + hra1 + esi1 + sa1)
net_salary = (bs + hra1 + sa1 - pf1 - esi1)
print("Your Gross Salary is",gross_salary)
print("Your Net Salary is",net_salary)  