def is_even(number):
    if number % 2 == 0:
        return True
    return False


def main():
    for num in range(1, 11):
        print(is_even(num))

if __name__ == "__main__":
    main()