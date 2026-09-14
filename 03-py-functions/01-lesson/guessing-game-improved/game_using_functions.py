import random
from game_helpers import *


def play_guessing_game():

    secret_number = random.randint(1, 30)
    result = ""

    while result != "correct":
        player_guess = read_guess()
        result = check_guess(player_guess, secret_number)
        show_feedback(result)


play_guessing_game()
