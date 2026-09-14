def read_guess():
    player_guess = int(input("Guess a number: (1-30) "))
    return player_guess


def check_guess(player_guess, secret_number):
    if player_guess == secret_number:
        return "correct"
    elif player_guess < secret_number:
        return "low"
    else:
        return "high"


def show_feedback(result):
    """Print correct/low/high"""
    if result == "correct":
        print("correct")
    elif result =="low":
        print("Too low")
    elif result == "high":
        print("Too high")
    else:
      print(f'Error, invalid result: "{result}"')