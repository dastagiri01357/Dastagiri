yr=int(input("Enter the year number:"))
mon=int(input("Enter month number:"))
if mon<=12:
    if (mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12):
        print("31 days")
    elif (mon==4 or mon==6 or mon==9 or mon==11):
        print("30 days")
    else:
        if yr%4==0 and mon==2:
            print("29 days")
        else:
            print("28 days")
else:
    print("invalid input")
        
