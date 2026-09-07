roof_number = int(input("Enter the highest number: "))
base_number = 1
multiplier = 1
while base_number < roof_number:
    base_number = multiplier * multiplier
    if base_number < roof_number:
        print(base_number)
    multiplier += 1
