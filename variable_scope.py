# global scope - is a e.g name which we can access inside and outside of function.
# local scope is a a e.g name which we can access only inside of our function.

user_name = 'CodingNewBie'


def add_feature():
    x = 5

    def change_features():
        global x
        x = 10

    print("Before: ", x)
    print("Change")
    change_features()
    print("After: ", x)


add_feature()
print("X = ", x)