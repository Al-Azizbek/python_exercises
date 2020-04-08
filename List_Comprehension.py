# let's see example to understand list comprehension

# classic way----------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * number)
print(doubled_numbers)

# List_Comprehension way----------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_numbers = [number * number for number in numbers]
print(doubled_numbers)
# Actually we can use for into list and by this way we can save new values inside it.


# Another List_Comprehension way----------------------------------------

numbers = [number for number in range(1, 101)]
doubled_numbers = [number for number in numbers if number % 2 == 0]
print(doubled_numbers)
# print even values in range of (1, 100)
