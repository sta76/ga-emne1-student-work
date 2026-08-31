first_number = int(input("Enter integer number 1-10: "))
second_number = int(input("Enter a second integer number 1-10: "))

while first_number > 0 < second_number:
    print(f"{first_number} + {second_number} = ", first_number + second_number)
    print(f"{first_number} - {second_number} = ", first_number - second_number)
    print(f"{first_number} * {second_number} = ", first_number * second_number)
    print(f"{first_number} / {second_number} = ", first_number / second_number)
    print(f"{first_number} // {second_number} = ", first_number // second_number)
    print(f"{first_number} % {second_number} = ", first_number % second_number)
    break
else:
    print("You entered a invalid number '0'")
