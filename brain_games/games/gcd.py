import random
import math
from brain_games.logic import answer
from brain_games.logic import welcome


def what_nod():
    a = random.choice(range(0, 100))
    b = random.choice(range(0, 100))
    nod_result = math.gcd(a, b)
    return (nod_result, str(a) + ' ' + str(b))


def brain_gcd():
    name_user = welcome()
    print("Find the greatest common divisor of given numbers.")
    i = 1
    while i <= 3:
        whatsnod = what_nod()
        question_user = whatsnod[1]
        right_answer = whatsnod[0]
        print(f'Question: {question_user}')
        answer_user = answer()
        if answer_user != str(right_answer):
            return print(f"{answer_user} is wrong answer ;(. \
Correct answer was {right_answer}. \
\nLet's try again, {name_user}!")
        print('Correct!')
        i = i + 1
    print(f'Congratulations, {name_user}!')
