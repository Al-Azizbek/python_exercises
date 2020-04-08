# Maps are use to operate certain type of operation on List --------------------------------
# list(map(function, list_data)) <- general view of map

def cal_sqrt(number):
    return number * number


user_score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # map will change value of each element into list

print(list(map(cal_sqrt, user_score)))  # output 1, 4, 9, 16 ... power of each number into list.


# Filters are used to filter certain type of list ---------------------------------------------
# list(filter(function, list_data)) <- general view of filter

def del_f(grade):
    return grade != 'F'


user_grade = ['A', 'B', 'F', 'C', 'F']
print(list(filter(del_f, user_grade)))  # output will be A, B, C bcz filter option help me to
# filter list and pick what i want into list
