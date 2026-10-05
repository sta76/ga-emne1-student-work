def calculate_tip(amount, tip_percent = 0):
    tip_amount = (amount * tip_percent)/100
    return tip_amount


def main():
    print(calculate_tip(100))
    print(calculate_tip(100, 5))

if __name__ == "__main__":
    main()