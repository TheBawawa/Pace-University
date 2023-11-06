def add():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(f"{num1} + {num2} = {num1 + num2}")


def subtract():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(f"{num1} - {num2} = {num1 - num2}")


def multiply():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(f"{num1} * {num2} = {num1 * num2}")


def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(f"{num1} / {num2} = {num1 / num2}")


def do_arithmetic():
    reply = ""

    while reply != "DONE":
        if reply == "":
            reply = input(
                "Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. "
            )
        elif reply == "+":
            add()
            reply = input(
                "Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. "
            )
        elif reply == "-":
            subtract()
            reply = input(
                "Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. "
            )
        elif reply == "*":
            multiply()
            reply = input(
                "Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. "
            )
        elif reply == "/":
            divide()
            reply = input(
                "Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. "
            )
        else:
            print("ERROR: Please enter a valid operator (i.e. +, -, *, /).")
            reply = input(
                "Would you like to add (+), subtract (-), multiply (*), or divide (/)? Enter DONE to end. "
            )


def main():
    print("Welcome to the S.E.B Calculator!")
    shutdown = input("Would you like to calculate (y), or shut down (n) ?")

    if shutdown == "y":
        do_arithmetic()

    reply02 = ""

    while reply02 != "n":
        reply02 = input("Would you like to continue operation? [y/n] ")
        if reply02 != "n":
            do_arithmetic()


main()
