# in python the to compare and do some expression, we use if/else statement.

student_name = input("Please enter your name: ")
student_age = int(input("Enter your age: "))

if student_age >= 18:  # is user age is equal to 18 and bigger than 18. print "Welc ..." message
    print(f"Welcome {student_name}")
else:  # else print below message to user.
    print(f"You age {student_age} is too young.")

# if/elif/else ----------------------------------------------------------
# more than 2 cases we have to use elif as an addition of if/else.

user_grade = input("Please enter your grade to see our point(A, B, C, D): ")

if user_grade == 'A' or user_grade == 'a':
    print("Your score is 5.")
elif user_grade == 'B' or user_grade == 'b':
    print("Your score is 4.")
elif user_grade == 'C' or user_grade == 'c':
    print("Your score is 3.")
else:
    print(print("Your score is 2."))
