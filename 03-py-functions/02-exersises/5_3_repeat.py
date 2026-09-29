def repeat_message(message, repetitons = 3):
    for i in range(repetitons):
        print(message)


def main():
    repeat_message("dette er en test")
    repeat_message("--------------------",1)
    repeat_message("dette er en ny test", 5)

if __name__ == "__main__":
    main()