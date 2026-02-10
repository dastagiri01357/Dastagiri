amt=int(input("Enter the purchase amount:")) 
print("1.500/-coupon code\n2.1000/- coupon code \n3.5000 coupon code")
cpn=int(input("Enter the coupon code number:"))
if cpn==1:
    amt=amt-amt*0.05
elif cpn==2:
    amt=amt-amt*0.1
elif cpn==3:
    amt=amt-amt*0.15
else:
    print("No Coupon Code")
print("The FInal amount is :",amt)


