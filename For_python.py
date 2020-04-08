# for loop in python work as the same with while loop but difference between them is. In For/Loop I don't have to
# declare and string or int.

user_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # create a list

for number in user_number:  # each element into list represent as number
    print(number)

# ----------------------------------------------------------------------
# below example also the same with above one but in this case, I don't have to create list
#  range(beginning of point, ending of point) generate list for me
for number in range(1, 10):
    print(number)

# ----------------------------------------------------------------------

user_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in range(len(user_number)):  # when i don't know the length of list I ve to us len method.
    print(number)
