weight = int(input("Enter the weight of the parcel in kg: "))
if weight < 11:
    if weight <= 2:
        price = 79
    elif 2 < weight <= 5:
        price = 129
    elif 5 < weight <= 10:
        price = 199
    print((f"It will cost you {price} to ship the parcel"))
else:
    print("The parcel is to heavy, can only be up to 10 kg")
