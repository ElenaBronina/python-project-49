import random
import math
from brain_games.logic import answer
from brain_games.logic import welcome


def is_prime(random_number):
    if random_number < 2:
        return 'no'
    if random_number == 2:
        return 'yes'
    limit = math.sqrt(random_number)
    i = 2
    while i <= limit:
        if random_number % i == 0:
            return 'no'
        i += 1
    return 'yes'


def brain_prime():
    name_user = welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i <= 3:
        random_number = random.randint(2, 30)
        print(f'Question: {random_number}')
        answer_user = answer()
        right_answer = is_prime(random_number)
        if answer_user == right_answer:
            print('Correct!')
        i = i + 1
        if answer_user != right_answer:
            return print(f"{answer_user} is wrong answer ;(. \
Correct answer was {right_answer}. \
\nLet's try again, {name_user}!")
    print(f'Congratulations, {name_user}!')
