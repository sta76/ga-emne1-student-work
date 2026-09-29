def ask_question(question_text):
    """Stiller spørsmål til brukeren, og returnerer svaret"""
    return input(question_text)



def check_answer(answer, correct_answer):
    """Returnerer True om svaret er riktig, False om feil"""
    if (answer == correct_answer):
        return True
    else:
        return False


def show_feedback(is_correct):
    """Gir tilbakemelding om bruker svarte riktig eller feil"""
    if is_correct == True:
        print("Du svarte riktig!")
    else:
        print("Du svarte feil!")
