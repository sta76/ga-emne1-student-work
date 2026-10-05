def ask_question(question_text):
    return input(question_text)



def check_answer(answer, correct_answer):
    if (answer == correct_answer):
        return True
    else:
        return False


def show_feedback(is_correct):
    if is_correct == True:
        print("Du svarte riktig!")
    else:
        print("Du svarte feil!")


def run_quiz():
    score = 0
    answer = ask_question("Hvilken hund er Leo?: ")
    is_correct = check_answer(answer, "stor puddel")
    if is_correct == True:
        score +=1
    show_feedback(is_correct)
    print()
    answer = ask_question("Hvilet kjønn er Leo: ")
    is_correct = check_answer(answer, "gutt")
    if is_correct == True:
        score += 1
    show_feedback(is_correct)

    print()

    answer = ask_question("Hvor gammel er Leo?: ")
    is_correct = check_answer(answer, "5")
    if is_correct == True:
        score += 1
    show_feedback(is_correct)
    print()
    print(f"Du hadde {score} riktige svar")


def main():
    run_quiz()
if __name__ == "__main__":
    main()