

def show_temp(city, temp):
    """Printer ut by og tilhørende temperatur"""
    print(f"I {city} er det {temp} grader")

def main():

    while True:

        city = input("Skriv inn navnet på byen: ").strip()

        if len(city) == 0:
            print("By navn kan ikke være tomt")
            continue
        elif city.isdigit():
            print("By navn kan ikke være tall")
            continue
        break

    while True:
        try:
            temp = int(input("Skriv inn temperaturen: "))
            break
        except ValueError:
            print("Bruk tall for temp")

    show_temp(city, temp)


if __name__ == "__main__":
    main()
