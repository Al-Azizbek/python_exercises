# lambda function in python known as anonymous function bcz while creating lamda function we don't have to give name.

# simple way without lambda ---------------------------------------------
numbers = [number for number in range(1, 11)]


def sqrt(n):
    return n * n


print(list(map(sqrt, numbers)))

# with lambda--------------------------------------------------------------

numbers = [number for number in range(1, 11)]
print(list(map(lambda n: n * n, numbers)))
# lambda function help to create function very easy.
# both examples results are the same
