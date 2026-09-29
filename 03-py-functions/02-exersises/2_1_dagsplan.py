
def show_daily_plan(aktivitet_1, aktivitet_2, aktivitet_3):
    """ Skriver ut 3 forskjellige aktiviteter"""

    return f"Her printer jeg ut aktivitet: {aktivitet_1}\nHer printer jeg ut aktivitet: {aktivitet_2}\nHer printer jeg ut aktivitet: {aktivitet_3}"

def main():

    funk_1 = show_daily_plan("fotball", "karate", "tennis")
    funk_2 = show_daily_plan("svømming", "jogging", "yoga")


    print(funk_1)
    print(funk_2)

if __name__ == "__main__":
    main()
