user_input = int(input("Enter the number of raw: "))

for i in range(user_input):
    for j in range(user_input):
        print("*", end="")
    print()
#print cube according to user input if user input is 4. Cube is 4 by 4.
#----------------------------------------------------------------------
user_input: int = int(input("Enter the number of raw: "))

for i in range(user_input):
    for j in range(i+1):
        print("*", end="")
    print()
#print triangle.
# ----------------------------------------------------------------------

user_input: int = int(input("Enter the number of raw: "))
for i in range(1, user_input+1):
    print('*' * i)
# print triangle with 1 for loop.
# ----------------------------------------------------------------------
user_input: int = int(input("Enter the number of raw: "))
for i in range(0, user_input):
    for k in range(0, i):
        print(" ", end="")
    for j in range(0, user_input - i):
        print("*", end="")
    print()
# print vise triangle.
# ----------------------------------------------------------------------
user_input: int = int(input("Enter the number of raw: "))
for i in range(0, user_input):
    for j in range(0, user_input-1):
        print("", end="")
    for k in range(0, i+1):
        print("*", end="")
    print()
# print 3 for loops triangle.
# ----------------------------------------------------------------------

user_input = int(input("Enter number of row:"))

for i in range(0, user_input + 1):

    print(" " * i + (user_input-i) * "*")
# print vise triangle with 1 for loop.
# ----------------------------------------------------------------------

user_input = int(input("Enter the number:"))
for i in range(1, user_input + 1):
    print(" " * (user_input - i) + (i * 2 - 1) * "*")
# print right triangle with 1 for loop.
# ----------------------------------------------------------------------


for j in range(1, user_input + 1):
    print((" " * j) + (user_input * 2 - j * 2 - 1) * "*")
# print rhombus with 1 for loop.
# ----------------------------------------------------------------------