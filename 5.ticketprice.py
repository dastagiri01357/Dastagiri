age=int(input("Enter your age:"))
height=float(input("Enter your height:"))
if age<=12:
    if height<=4:
        print("Ticket price is $10")
    else:
        print("Ticket price is $15")
else:
    print("Ticket price is $20")
