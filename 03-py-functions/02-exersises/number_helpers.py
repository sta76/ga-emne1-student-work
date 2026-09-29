def find_largest(first_number, second_number):
    """ Får inn 2 tall og returnerer om det ene er større ellr lik det andre"""
    if first_number < second_number:
        return second_number
    elif first_number > second_number:
        return first_number
    else:
        return first_number == second_number


def is_even(number):
    """Returnerer True dersom ett tall er partall, False om oddetall"""
    if number % 2 == 0:
        return True
    return False