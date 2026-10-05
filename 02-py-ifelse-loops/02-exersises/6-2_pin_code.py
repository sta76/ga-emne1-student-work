secret_pin = 2468
attempts_left = 3


while attempts_left != 0:
    test_pin = int(input("Enter your pin code: "))
    attempts_left -= 1
    if test_pin == secret_pin:
        print("Access granted")
        break
    elif attempts_left > 0:
        print(f"Wrong code, you have {attempts_left} left")
else:
    print("Access denied")

