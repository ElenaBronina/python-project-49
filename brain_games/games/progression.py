import random
from brain_games.logic import answer
from brain_games.logic import welcome


def progression():
    a = random.choice(range(5, 10))
    b = random.choice(range(20, 100))
    c = random.choice(range(2, 10))
    progression = list(range(a, b, c))
    i = progression.index(random.choice(progression))
    n = progression[i]
    return (progression, i, n)


def brain_progression():
    name_user = welcome()
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        exercise = progression()
        question_user = exercise[0]
        right_answer = exercise[2]
        question_user[exercise[1]] = ("..")
        print(f'Question: {question_user}')
        answer_user = answer()
        if answer_user != str(right_answer):
            return print(f"{answer_user} is wrong answer ;(. \
Correct answer was {right_answer}. \
\nLet's try again, {name_user}!")
        print('Correct!')
        i = i + 1
    print(f'Congratulations, {name_user}!')
