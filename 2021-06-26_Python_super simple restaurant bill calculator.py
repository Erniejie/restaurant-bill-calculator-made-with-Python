#super simple restaurant bill calculator made with Python
#computer programming tutor,23 June 2021

#1. Prompting user for  the food charging fees

food_charge = float(input("Enter Amount of Money for Ordered Food,[£]:"))

#2. Configure Tip Amount

service =20/100*food_charge
print("Your Service Charge is[£]: ", format(service,".2f"))

# 3. Configure the sale tax

sales_tax = 8/100*food_charge

print("Your Sales Tax is[£]: ", format(sales_tax ,".2f"))

#4. Total Amount

total_amount=food_charge + service + sales_tax
print("Your Total Amount is[£]: ", format(total_amount ,".2f"))
