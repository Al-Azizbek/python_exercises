# pickle in python help to us to create bunch of text which only computer can read and analyse
import pickle  # have to import pickle

# let's see how to turn list into pickle--------------------------------------------------------------
user_names = {
    1: "CodingNewBie",
    2: "Google",
    3: "YouTube",
    4: "Apple"
}

pickle_file = open("/Users/name/Downloads/github_my_all/Python_exercises/Pickle/CodingNewBie.txt", "wb")

pickle.dump(user_names, pickle_file)

pickle_file.close()

# let's see how to turn pickle to text

pickle_new = open("/Users/name/Downloads/github_my_all/Python_exercises/Pickle/CodingNewBie.txt", "rb")
example_dic = pickle.load(pickle_new)

print(example_dic)
