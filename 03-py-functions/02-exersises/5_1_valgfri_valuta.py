def show_price(price, currency = "NOK"):
    print(f"{price} i {currency}")


def main():
    show_price(250)
    show_price(25,"EUR")

if __name__ == "__main__":
    main()