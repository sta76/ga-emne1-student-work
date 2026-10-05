from quiz_helpers import *

def run_quiz():
    score = 0
    answer = ask_question("Hvilken hund er Leo?: ")
    is_correct = check_answer(answer, "stor puddel")
    if is_correct:
        score +=1
    show_feedback(is_correct)
    print()
    answer = ask_question("Hvilet kjønn er Leo: ")
    is_correct = check_answer(answer, "gutt")
    if is_correct:
        score += 1
    show_feedback(is_correct)

    print()

    answer = ask_question("Hvor gammel er Leo?: ")
    is_correct = check_answer(answer, "5")
    if is_correct:
        score += 1
    show_feedback(is_correct)
    print()
    print(f"Du hadde {score} riktige svar")


def main():
    run_quiz()
if __name__ == "__main__":
    main()