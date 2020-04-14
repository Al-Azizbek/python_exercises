import random

user_name = input("Enter your name:")
user_age = int(input("Enter your age: "))
if user_age > 18:
    user_balance = int(input("Enter your balance(make sure your balance more than 50):"))
    if user_balance >= 50:
        print("Welcome to my casino.")
        print("Rule of casino game: \n")
        print("Below there will be 3 dices. Bet to the Small or Big.\n"
              "1-12 Small | 12-18 Big")

        user_choice = int(input("1 : Play | 0 : Stop"))
        while user_choice != 0:
            user_bet = input("SMALL|BIG : ")

            num_one = random.randint(1, 7)
            num_two = random.randint(1, 7)
            num_third = random.randint(1, 7)

            sum_num = num_one + num_two + num_third
            print(" --------------")
            print(f"| {num_one} || {num_two} ||  {num_third} |")
            print(" --------------")
            if user_bet == "small" or user_bet == "SMALL" or user_bet == "Small" or user_bet == "big" or user_bet == "BIG" or user_bet == "Big":
                if sum_num < 12:
                    print("SMALL WIN")
                    if user_bet == "small" or user_bet == "SMALL" or user_bet == "Small":
                        print(f"{user_name}, your balance is now: ", user_balance + 30)
                        user_balance = user_balance + 30
                    else:
                        print(f"{user_name}, your balance is now: ", user_balance - 10)
                        user_balance = user_balance - 10
                else:
                    print("BIG WIN")
                    if user_bet == "big" or user_bet == "BIG" or user_bet == "Big":
                        print(f"{user_name}, your balance is now: ", user_balance + 30)
                        user_balance = user_balance + 30
                    else:
                        print(f"{user_name}, your balance is now: ", user_balance - 10)
                        user_balance = user_balance - 10
                    print(50 * "-")
                    user_choice = int(input("1 : Play | 0 : Stop"))
            else:
                print("Invalid choice or you wanna miss this chance.")
    else:
        print("Sorry, You can't play this game. Bcz your balance is less than 50. To play this game your balance "
              "should be more than 50.")
else:
    print(f"Hello, {user_name}. Sorry your age is {user_age} and it is too young. 'AGE RESTRICTION.'")
