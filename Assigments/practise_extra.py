# lambda practises

double_number = lambda x: x * 2
print(double_number(2))

# find even and odd number

enenOdd = (lambda x: 'odd' if x % 2 else 'even')

print(enenOdd(int(input('Enter: '))))

# IIFE in lambda

for i in range (6):
    print((lambda x: x**2)(i))

# multiple arguments with lambda

multipe_arg = lambda x, y, z: x + y + z
print(multipe_arg(1, 2, 3))  # or

several_arg = lambda *args: sum(args)
print(several_arg(1, 2, 3))  # or

several_arg = lambda **kwargs: sum(kwargs.values())
print(several_arg(x = 1, y = 2, c= 3))

# map function example take 2 arguments 1 st function 2 nd list

def double_number(x):
    return x*2

my_list = [i for i in range (101)]

my_final = map(double_number, my_list)

print(list(my_final)) # with traditional function

with_lambda = map(lambda x: x**2, my_list)
print(list(with_lambda)) # map function with lambda

# filter funtion, we can use it to filter the one function and List and filter just return the True not False

def check_age(user_age):
    if user_age >= 18:
        return True
    else:
        return False
age = [i for i in range (10, 30, 3)]

age_filter = filter(check_age, age)
print(list(age_filter)) # with def function and checking the filter()

check_age = filter(lambda age_user : age_user > 18, age )
print(list(check_age)) # with lambda

# reduce() which we can use is t rolling calculator

from functools import reduce

def cal_sum(a,b):
    return a+b
L = [i for i in range(100)]

total = reduce(cal_sum, L)
print(total)

calculatons = reduce(lambda x,y: x + y, L)
print(calculatons)

user_number = [i for i in range(6)]
print(user_number)

# class and objects

class Car:
    pass

 # __init__() is initializes an individual object or method is generallu used to perform operations that are necessary before the object created

# Access and modify attributes of an object
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

c = Car('Black', 'Sedan')

# Access attributes
print(c.style)
# Prints Sedan
print(c.color)
# Print

# open, write a file in Python

open_file = open('/Users/macbook/Documents/new.txt')
for line in open_file:
    print(line) # print all txt lines as list

open_file = open("/Users/macbook/Documents/new.txt", 'w')
open_file.write('My name is Not Azizbek.')

open_file = open("/Users/macbook/Documents/new.txt", 'r+')
open_file.write('My name is Not Aziz.')
print(open_file.readlines())

open_file.flush() # is store the new variable without closing the file

open_file.close() # is to close the opened file

print(open_file.closed)

with open("/Users/macbook/Documents/new.txt") as f:
    print(f.read()) # is easy and safe way of closing the opened file

open_file = open("/Users/macbook/Documents/new.txt")

try:
  # File operations goes here
finally:
    f.close() # the second approach to close the opened file

# deleting the file

import os

os.remove('/Users/macbook/Documents/new.txt') # remove the file

open_file = open("/Users/macbook/Downloads/total.csv", 'r+')
print(open_file.readlines(5))

# work with csv files

import csv

with open("/Users/macbook/Downloads/total.csv", 'r+') as my_new_practise:
    new_view = csv.DictReader(my_new_practise)
    for row in new_view:
        print(row)

# csv.reader - can be use only when we want to open the simple csv but when we use the keyword DictReader it means we can open the csv and also automatically save the first raw as the main attratbute names
