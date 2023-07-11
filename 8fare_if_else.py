n = input("Enter Name: ")
age = int(input("Enter Age: "))
g = input("Enter Gender Male or Female: ")
km = int(input("Enter Kilometre: "))
w = input("Enter Good and Bad: ")
tm = input("Enter Day and Night: ")
trf = input("Enter Traffic Yes or No: ")
dense = input("Enter Density Yes or No : ")

final_amt = km * 5

age_discount = 0
if(age >= 60):
    age_discount = final_amt * 2 / 100
    final_amt = final_amt - age_discount

gender_discount=0
if(g == "female" or g == "Female"):
    gender_discount = final_amt * 5 / 100
    final_amt = final_amt - gender_discount

weather_charges=0
if(w == "Bad" or w == "bad"):
    weather_charges = final_amt * 2 / 100
    final_amt = final_amt + weather_charges

time_Charge=0
if(tm == "day" or tm == "Night"):
    time_Charge = final_amt * 1 / 100
    final_amt = final_amt + time_Charge

traffic_charges=0
if(trf == "Yes" or trf == "yes"):
    traffic_charges = final_amt * 2 / 100
    final_amt = final_amt + traffic_charges

dense_charges=0
if(dense == "Yes" or dense == "yes"):
    dense_charges = final_amt * 5 / 100
    final_amt = final_amt + dense_charges

print("Your Final Fare is",final_amt)