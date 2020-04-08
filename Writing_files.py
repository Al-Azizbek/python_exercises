# There are 2 ways of writing files in python
# ---------------------------------------------------
# just using simple way
file = open("file_name.txt", 'w', encoding="ISO-8859-1")

file.close()  # its some time annoying. So let's use another option.

# ---------------------------------------------------
# by using the with/as

with open("file_name.txt", 'w', encoding="ISO-8859-1") as writing_file_example:  # "just identify with "w"
    writing_file_example.write("Hello my name is CodingNewBie")  # write command and start writing.
    # But Don't forget when I use "w" keyword it takes file and I will write something. But whatever I type inside is
    # new.
