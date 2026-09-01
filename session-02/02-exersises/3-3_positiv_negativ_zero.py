number = int(input("Enter a integer, can be positive, negative or zero: "))
check_number = 'odd'

if number % 2 == 0:
    check_number = 'even'
if number == 0:
    print("Number is zero")
elif number < 0:
    print(f"Number is negative and a {check_number} number")
else:
    print(f"Number is positive and a {check_number} number")
