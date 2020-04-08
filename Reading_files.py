# There are 2 ways of reading files in python
# ---------------------------------------------------
# just using simplel way
file = open("file_name.txt", 'r', encoding="ISO-8859-1")
file.seek('CodingNewBie')  # search certain character
for line in file:
    print(line)  # print all lines inside of .txt file
    print((line.rstrip()))  # lose gaps among paragraphs
    print(line.lower())  # turn all words inside .txt into lower letter.
    # also there are bunch of methods which I can use with "line"
# but every time when I opened the file I have to close it

file.close()  # its some time annoying. So let's use another option.


# ---------------------------------------------------
# by using the with/as
def sequence_filter(line):
    return "-" not in line  # define a function which scrawl whole text and pick lines without starting "-"


with open("file_name.txt", 'r', encoding="ISO-8859-1") as reading_file_example:
    lines = reading_file_example.read()
    # lines = reading_file_example.readlines()
    print(
        list(filter(sequence_filter, lines)))  # use filter which take function = seuquence_filter and also data = lines
