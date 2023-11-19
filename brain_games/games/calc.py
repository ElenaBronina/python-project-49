import random
from brain_games.logic import answer
from brain_games.logic import welcome


def brain_calc():
    name_user = welcome()
    print('What is the result of the expression?')
    i = 1
    while i <= 3:
        num_1 = random.choice(range(0, 30))
        num_2 = random.choice(range(0, 30))
        oper = random.choice(['+', '*', '-'])
        right_answer = int(eval(f'{num_1} {oper} {num_2}'))
        print(f'Question: {num_1} {oper} {num_2}')
        answer_user = answer()
        if answer_user != str(right_answer):
            return print(f"{answer_user} is wrong answer ;(. \
Correct answer was {right_answer}. \
\nLet's try again, {name_user}!")
        print('Correct!')
        i = i + 1
    print(f'Congratulations, {name_user}!')
