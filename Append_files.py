# There are 2 ways of Appending files files in python
# ---------------------------------------------------
# just using simple way
file = open("file_name.txt", 'a', encoding="ISO-8859-1")

file.close()  # its some time annoying. So let's use another option.

# ---------------------------------------------------
# by using the with/as

with open("file_name.txt", 'a', encoding="ISO-8859-1") as writing_file_example:  # "just identify with "a"
    writing_file_example.write("Hello my name is CodingNewBie")  # write command and start writing.
    # when u start appending file it means, your are not writing from beginning you just append file
