number1 = int(input("Enter a number and press enter: "))
number2 = int(input("Enter another number and press enter: "))

# The same but only 1 line of code
# number1, number2 = map(int, input("Enter two number separated with space: ").split())

addition = number1 + number2
multiplication = number1 * number2

print(f"{number1} + {number2} is {addition}")
print(f"{number1} * {number2} is {multiplication}")
