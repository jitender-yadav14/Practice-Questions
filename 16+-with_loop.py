'''(1) + (1+2) - (1+2-3) + (1+2-3+4)'''
a = int(input("Enter the Numbe:- "))
outer_sum = 2
for i in range(1,a + 1):
    inner_sum = 2
    for j in range(2,i + 1):
        if(j % 2 == 0):
            inner_sum += j
        else:
            inner_sum -= j
        if(i % 2 == 0):
            outer_sum += inner_sum
        else:
            outer_sum -= inner_sum
print(outer_sum)