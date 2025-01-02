print("=========== WELCOME ============")
print("Press [1] For Rajhans Cinema")
print("Press [2] For Cinepois")
print("Press [3] For PVR")

ch = int(input("Enter Your Choice : "))

if ch ==1:
    print("=========== WELCOME TO RAJHANS CINEMA ============")
    print("Press [1] for Standard : 120 per Seat")
    print("Press [2] for Recliner : 160 per Seat")
    print("Press [3] for VIP : 200 per Seat")

    ch1 = int(input("Enter Your Choice : "))
    price = int(input("Enter Number Of Seats : "))
    if ch1==1:
        print("Total Bill : ",120*price)

    elif ch1==2:
        print("Total Bill : ",160*price)

    elif ch1==3:
        print("Total Bill : ",200*price)
    
    else:
        print("Invalid Seat Choice !!!")