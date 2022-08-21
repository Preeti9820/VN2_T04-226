#Write a program to determine how much discount a customer can get based on the below conditions:
# A customer gets the following discounts based on the respective criteria:
# 1.	15 % on first purchase at the store.
# 2.	10 % if he/she has a membership card
# 3.	5% if senior citizen
# 4.	10 % on coupons
# Note:
# 1.	Only 2 discounts can be clubbed together, any 2 that give the highest discount
# 2.	New customers cannot redeem coupons or get membership card discount

# Sample output:
# Eg 1: Customer is senior citizen and has a membership card
# Output: 15%
# Eg 2: Customer is senior citizen and has both coupon and membership card
# Output: 20%


visit=input("enter First time or not: Y / N ")
member=input("enter Member or not: Y / N ")
age= int(input("enter age"))
coupons=input("enter having Coupon or not: Y / N ")
if visit =='Y':
    if age >= 55:
        print("the Customer will get 20% of discount")
    else:
        print("the Customer will get 15%")
elif age >=55:
    if member=='Y':
        print("the customer wil;l get 15%")
    elif coupons =='Y':
        print("the customer will get 15%")
elif member =='Y' and coupons =='Y':
    print("the customer will get 20%")
else:
    print("the customer will get 10%")


