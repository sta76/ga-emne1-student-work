def greet_student(name):
    print(f"Velkommen {name}")

def main():
    name1 = input("Hva er navnet ditt: ")
    greet_student(name1)
    name2 = input("Hva er navnet ditt: ")
    greet_student(name2)
    name3 = input("Hva er navnet ditt: ")
    greet_student(name3)
    
if __name__ == "__main__":
    main()