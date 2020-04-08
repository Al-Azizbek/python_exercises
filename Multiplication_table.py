# to print multiplication table I have to use nested for loop

print("Welcome to Multiplication table:\n")
for row in range(1, 10):
    for column in range(1, 10):
        print(f"{row} x {column} = {row * column}")
    print("-" * 10)



