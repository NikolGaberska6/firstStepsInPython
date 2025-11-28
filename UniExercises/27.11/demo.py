def ex_1():
    print("Gimme your file name: ", end="")
    file_name = input()
    print_info_from_file(file_name)


def ex_2():
    try:
        number = float(input("Number: "))
        get_sqrt_number(number)
    except ValueError:
        print("Number bro, number")


def ex_3():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        n = int(input("Gimme number: "))
        if n <= 0 or n > len(days):
            raise ValueError
        print(days[n - 1])
    except ValueError:
        print("Invalid number")


def ex_4():
    try:
        length = float(input("Length: "))
        width = float(input("Width: "))

        if length <= 0 or width <= 0:
            raise ValueError

        print(f"The area is {length * width}")
    except ValueError:
        print("Invalid number")


def ex_5():
    try:
        number = float(input("Number to be checked if it is divisible by 3 and 5: "))

        if number % 3 == 0 and number % 5 == 0:
            print("Divisible")
        else:
            print("Not Divisible")
    except ValueError:
        print("Invalid number")


def ex_6():
    try:
        year = float(input("Year to be checked if it is a leap year: "))

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("Is leap")
        else:
            print("Is not leap")
    except ValueError:
        print("Invalid number")


def get_sqrt_number(number=1.0):
    try:
        print(f"Byee with {float(number ** (1 / 2)):.5f}")
    except TypeError:
        print("Invalid number")


def print_info_from_file(file_name):
    try:
        with open(file_name) as file:
            for line in file:
                print(line, end="")
        print("")
    except FileNotFoundError:
        print("Sry wrong file. ", end="")


def main():
    while True:
        try:
            option = int(input("What program u wanna run:\n"
                               "1. Read file\n"
                               "2. Get sqrt of number\n"
                               "3. Days in week\n"
                               "4. Area of a rectangle\n"
                               "5. Check if a number is divisible by 3 and 5\n"
                               "6. Check if a year is a leap year\n"
                               "Your option: "))

            func = globals().get(f"ex_{option}")
            if func:
                func()
            else:
                continue
        except ValueError:
            print("Number bro")


if __name__ == "__main__":
    main()
