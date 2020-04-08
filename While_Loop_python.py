# for loops in python can help us to do some tpe of task recently.

# user_numbers = [number for number in range(1, 101)]  # generate numbers list from 1 to 100 and save as list.
#
# while user_numbers != 101:
#     print(user_numbers)  # creates 101 row each row has 101 elements


# simple example-------------------------------------------------------------------------------

user_age = 25
number = 0
while number < 25:
    print(number)
    number += 1  # add 1 each time
# print numbers from 1 to 25 when number greater than user_age while loop will stop

# simple example01-------------------------------------------------------------------------------

user_age = 25
number = 0
while number < 25:
    print(number)
    number += 1
    if number == 10:
        print("I am 10.")
    elif number == 20:
        print("I am 20.")
    else:
        print("I am value.")

# ODD/EVEN-------------------------------------------------------------------------------
# program will take input from user and find it ODD or EVEN. If user input is 0 while loop will stop.

user_number = int(input("Enter the number to check odd or even: "))
while user_number != 0:

    if user_number % 2 == 0:
        print(f'{user_number} is EVEN.')
    else:
        print(f'{user_number} is ODD.')

    user_number = int(input("Enter the number to check odd or even: "))
