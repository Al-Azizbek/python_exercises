#Multplication Table by using the Nested for loops and also format string.
# {0:2} is used to give space and also {2:<2} stick elements to left side
#imagine {row : space_limit} and {col : space_limit}

for row in range(1, 11):
    for col in range(1, 11):
        print("{0:2} x {1:2} = {2:<2}\t".format(row, col, row * col), end='|')
    print()