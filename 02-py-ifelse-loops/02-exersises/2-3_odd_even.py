number = int(input("Enter a integer: "))

number_p_2 = number ** 2
number_p_3 = number ** 3
reminder = number % 2

print(f"{number} ** 2 is {number_p_2}")
print(f"{number} ** 3 is {number_p_3}")
print(f"{number} % 2 is {reminder}")
if reminder == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is a odd number")
