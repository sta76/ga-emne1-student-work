secret_number = 21
attempts_left = 5
guessed_correctly = False


while attempts_left > 0 and not guessed_correctly:
    guess = int(input("Enter a number between 1-30: "))
    if guess > secret_number:
        print("Try lower")
    elif guess < secret_number:
        print("Try higher")
    else:
        print("You guessed correctly")
        print((f"You had {attempts_left} left"))
        guessed_correctly = True
    attempts_left -= 1
if not guessed_correctly:
    print(f"The number was {secret_number}")