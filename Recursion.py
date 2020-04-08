# recursion actually function repeat itself and its called recursion.

import sys

try:
    print(sys.getrecursionlimit())  # to check the limit of recursion
    sys.setrecursionlimit(2000)  # set the recursion limit by default
    number = 0


    def say_hello():
        global number
        number += 1
        print(f'{number}. Hello my name is CodingNewBie.')
        say_hello()  # this is recursion which is say_hello function is calling itself inside of say_hello function.


    say_hello()
except:
    print("Here is the 1996 times function called itself bcz I set up limit to 2000 at the top.")
