
def read_number():
    return int(input("Skriv inn en heltall du vil analyserer: "))


def describe_sign(number):
    sign = "-"
    if number < 0:
        sign = "negative"
        return sign
    elif number == 0:
        sign = "zero"
        return sign
    sign = "positive"
    return sign


def is_even(number):
    even = False
    if number % 2 == 0:
        even = True
        return even
    return even


def show_analysis(number, sign, even):
    print(f"Tallet {number} er {sign}. Er det et partall: {even}")


def run_number_analyser():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)
    show_analysis(number, sign, even)


def main():
    run_number_analyser()

if __name__ == "__main__":
    main()