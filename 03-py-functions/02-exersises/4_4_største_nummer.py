def find_largest(first_number, second_number):
    if first_number < second_number:
        return second_number
    elif first_number > second_number:
        return first_number
    else:
        return first_number == second_number


def main():

    print(find_largest(15, 10))
    print(find_largest(15, 20))
    print(find_largest(15, 15))

if __name__ == "__main__":
    main()