# create function tjat accept two vaiables and calculate + and - with the single return
#
# def my_func(a, b):
#     sum = a + b
#     minus = a - b
#     return sum, minus
#
# print(my_func(1,2))

# write a program that create recruation which calls itself again and again to calculate 1 to 10


# write a function which returns the even numbers between 50 to 100
# def my_func():
#     even_number = []
#     for i in range(50, 101):
#         if i % 2 == 0:
#             even_number.append(i)
#     print(even_number)
#
#
# print(my_func())

# write a code return alphabet letter as a value and index as a key :

# import string


# def zip_aplhabet():
#     eng_alphabet = list(string.ascii_uppercase)
#
#     number_set = []
#     for i in range(27):
#         number_set.append(i + 1)
#
#     make_zip = zip(eng_alphabet, number_set)
#
#     print(dict(make_zip))
#
#
# print(zip_aplhabet())

# find largest in the list by using the function

import random

random_list = []

number_limit = 2000

for i in range(number_limit):
    random_list.append(random.randint(1, 2000))
print(max(random_list))
 