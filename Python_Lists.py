# List in Python can save different types of elements like numbers, strings etc.

user_message = "Hello, my name is CodingNewBie."
print(user_message.split())  # convert string to Lists
# ------------------------------------------------------------
user_List01 = [1, 2, 3, 4, 5]  # list 1
user_List02 = [6, 7, 8, 9, 10]  # list 2

user_list_total = user_List01 + user_List02
print(user_list_total)  # one list consists of 10 elements 5 from list 1 and  others from list 2

# changing the list item -----------------------------------------------------

user_List01 = [1, 2, 3, 4, 5]

user_List01[0] = 11
print(user_List01)  # now first item of list which is 1 is changes to 11.

# appending the list item -----------------------------------------------------

user_List01 = [1, 2, 3, 4, 5]
user_List01.append(1)  # append is used to add 1 value to the end of the list.
print(user_List01)

# removing the list item -----------------------------------------------------

user_List01 = [1, 2, 3, 4, 5]

user_List01.pop()  # remove element from the end
user_List01.pop(0)  # remove element by index number of it.
user_List01.remove(2)  # remove element by itself.
del (user_List01[0])  # delete element by index
print(user_List01)

# list inside list -------------------------------------------------------------

user = [['Coding', 'New', 'Bie'], [1, 2, 3]]
print(user[0])
print(user[1])
print(user)
