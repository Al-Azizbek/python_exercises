# write the code to print first 10 integers and their square by using while loop :

number = 1
while number < 10:
    number += 1
    print(number * number)

# write program which print first 10 natural numbers in reverse order with using while loop

natural_number = 11
while natural_number >= 1:

    natural_number = natural_number - 1
    print(natural_number)

# get multiple inputs from the user and get the largest one among them.

print('Total you can input 5 number: ')

numbers = []
try_number = 0
while try_numbers < 5:
    try_numbers += 1
    user_number = int(input(f'Enter the {try_numbers} numbers: '))
    numbers.append(user_number)
    max_number = max(numbers)
print(f"{max_number} is the biggest number in you set.")
_numbers = 0

# get multiple inputs from the user and calculate avarage of them.

print('Total you can input 5 number: ')

total = 0
my_list = []
while total < 5:
    total += 1
    user_number = int(input(f'Enter the {total} number : '))
    my_list.append(user_number)
    avarage = (sum(my_list) / 5)
print(f'The avarage of your five inputs is {avarage}.')

# calculate the sum of numbers until the user enter 0 :

total = 1
user_inputs = []

while total < 100:
    total += 1
    user_number = int(input('Enter the number and O break the program : '))
    if user_number != 0:
        user_inputs.append(user_number)
        final = sum(user_inputs)
        print(final)
    else:
        break



