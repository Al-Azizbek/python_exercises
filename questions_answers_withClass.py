
__________Folder_name: question_class.py_____________________________
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class User:
    def __init__(self, user_name, user_surname, user_age):
        self.user_name = user_name
        self.user_surname = user_surname
        self.user_age = user_age
        print(f'Welcome {user_name} {user_surname}. Your age is {user_age}')
_______________________________________________________________________

from question_class import Question, User

try:
    user1 = User(
        input('Enter your name:'),
        input('Enter your Surname: '),
        input('Enter our age:'),

    )

except ValueError:
    print('Please enter your age as Int not as str.')


questions_examples = [
    'What is the value of PI? \n a)3.14\n b)2.14\n c)214.2\n',
    'What color girls like most? \n a)red\n b)blue\n c)green\n',
    'What color is sky? \n a)Blue\n b)Green\n c)Light grey\n',
    'What is the capital of South Korea? \n a)Busan\n b)Ulsan\n c)Seoul\n',
    'How many colors are exist in rainbow? \n a)11\n b)12\n c)13\n',
]

questions = [
    Question(questions_examples[0], 'a'),
    Question(questions_examples[1], 'a'),
    Question(questions_examples[2], 'a'),
    Question(questions_examples[3], 'c'),
    Question(questions_examples[4], 'b'),

]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'{score} / {len(questions)}')


run_quiz(questions)
