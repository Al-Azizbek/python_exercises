# Dictionaries in python use to save sertain type of date with its value and key.

user_names = {
    1: 'CodingNewBie',
    2: 'Chrome',
    3: 'Mozilla',
    4: 'YouTube',
    5: 'Google'
}
# example to create dictionary

user_keys = user_names.keys()
user_values = user_names.values()
print(user_keys)  # print keys of dictionaries 1, 2, 3, 4, 5
print(user_keys)  # print valuable of dictionary CodingNewBie, Chrome ...

# Convert value/key into lists -------------------------------------------------------


user_list = (list(user_names.keys()))
print(user_list)  # output [1, 2, 3, 4, 5] like as list

user_list = (list(user_names.values()))
print(user_list)  # output keep values of dictionary into list

print(user_list.count('CodingNewBie'))  # count certain value inside of list
print(sorted(user_list))  # sort certain list

# Dictionary as a for loop ------------------------------------------------------------


user_names = {
    1: 'CodingNewBie',
    2: 'Chrome',
    3: 'Mozilla',
    4: 'YouTube',
    5: 'Google'
}


def CodingNewBie(user_names):
    for key, val in user_names.items():
        print(key, val)


CodingNewBie(user_names)
