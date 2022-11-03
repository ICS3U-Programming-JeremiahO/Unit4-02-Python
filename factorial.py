#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: October 31 2022
# This program gets a year from a user, checks and display wether the year is a leap year or not


def main():
    # define variables
    loop_counter = 0
    factorial_answer = 1

    # get the user input
    User_number_as_string = input("Enter a positive number: ")
    print()
    try:
        User_number_as_int = int(User_number_as_string)

    except Exception:
        print()
        print("Please enter a positive integer (whole number).")
        exit()
    if User_number_as_int <= 0:
        print("Please enter a positive number (whole number). ")
        exit()

    # a do while loop
    # process calculate the factorial 0f user input using a loop format
    while True:
        loop_counter = loop_counter + 1
        factorial_answer = factorial_answer * loop_counter
        print("Tracking {} times through the loop.".format(loop_counter))
        if loop_counter >= User_number_as_int:
            break

    print()
    print("{} is the factorial of {}.".format(factorial_answer, User_number_as_int))


if __name__ == "__main__":
    main()
