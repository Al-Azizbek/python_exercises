#  write a program to print the last digit of a number :

number = 105

if number > 0 or number < 0:
    last_digit = number % 10
    print(f"{last_digit} is the last digit.")
else:
    print(f"{number} is not actual number.")

# write a program that converts kg  to pounds and pounds to kg

user_input = int(input('Please enter KG to convert POUND : '))

if user_input > 0:
    pound_convert = user_input * 2.2046
    print(f'{user_input} Kg is equal to {pound_convert} Pounds.')
else:
    print(f"{user_input} is not number.")

user_input_second = int(input('Please enter POUND to convert KG : '))

if user_input > 0:
    kg_convert = user_input_second % 2.2046
    print(f'{user_input_second} Pound is equal to {kg_convert} Kg.')
else:
    print(f"{user_input_second} is not number.")

# Write a program that converts Celcus to Fahrenheit and vise versa

celcius = 37
fahrenheit = (celcius * 1.8) + 32
print(f'{celcius} Celcuis is equal to {fahrenheit} Fahrenheit')

fahrenheit_one = 99.5
celcius_one = (fahrenheit_one - 32) / 1.8
print(f'{fahrenheit_one} Fahrenheit is equal to {celcius_one} Celcuis.')

# write a program which checks lap year or not :

user_year = int(input('Enter the year to check the Lap or Not : '))
if (user_year % 400 == 0) or (user_year % 4 == 0 and user_year % 100 != 0):
    print("This is a Lap Year")
else:
    print("This is Not a Lap Year")

# write the code which get two inputs from the user and find the biggest one :

number_first = int(input("Enter the first number : "))
number_second = int(input("Enter the second number : "))

if number_first > number_second :
    print(f"{number_first} is the biggest number.")
elif number_second > number_first :
    print(f"{number_second} is the biggest number.")
else:
    print(f"{number_first} and {number_second} are equal.")


# write the program which gets user score and evaluate it:

user_score_input = int(input("Enter your score :"))

if user_score_input >= 80 and user_score_input <= 100:
    print('Your score is A.')
elif user_score_input >= 60 and user_score_input < 80:
    print('Your score is B.')
elif user_score_input >= 30 and user_score_input < 60:
    print("Your score is C.")
else:
    print("You failed the exam and get F score.")