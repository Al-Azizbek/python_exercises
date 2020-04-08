# In here, I tried to use 2 ways of printing factorial of number

# first way is just using for, and if/else condition
user_input = int(input('Enter the number:'))

factorial = 1

if user_input < 0:
    print('Invalid input')
elif user_input == 0:
    print('Factorial 0 of is 1.')
else:
    for number in range(1, user_input + 1):
        factorial = factorial * number
    print(f'Factorial of {user_input} is {factorial}.')



# second way is by using recursion
def factorial_number(number):
    if number == 0:
        return 1
    return number * factorial_number(number - 1)


avg = factorial_number(5)
print(avg)
