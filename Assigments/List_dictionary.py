# write a program which print numbers frm 10 to 50 with step of 5 by using list comprehension

number_range = [i for i in range(10, 55, 5)]
print(number_range)

# create a prgram which shows sqares of from 10 to 50 by step 5 by using list cmprehension'

number_range = [i * i for i in range(10, 55, 5)]
print(number_range)

# create the program which shows numbers more than 100 by using 2nd program

number_range = [i * i for i in range (10, 55, 5) if i*i > 100]
print(number_range)

# create a dictionary with given details

di = {
    'Sedan': 1500,
    'SUV': 2000,
    'Pickup': 2500,
    'Sinivan': 1600,
    'San': 2400,
    'Semi': 13600,
    'Bycicle': 7,
    'Motorcycle ': 110
}

show_result = [value for key, value in di.items() if 2000 < value < 5000]
print(show_result)

# with the same dictionary on the above make key names uppercase

di = {
    'Sedan': 1500,
    'SUV': 2000,
    'Pickup': 2500,
    'Sinivan': 1600,
    'San': 2400,
    'Semi': 13600,
    'Bycicle': 7,
    'Motorcycle ': 110
}
uppercase_letter = [key.upper() for key in di.keys()]
print(uppercase_letter)
