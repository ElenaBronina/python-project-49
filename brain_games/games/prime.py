import random
import math
from brain_games.logic import answer
from brain_games.logic import welcome


def is_prime():
    random_number = random.randint(2, 25)
    if random_number < 2:
        return False
    if random_number == 2:
        return True
    limit = math.sqrt(random_number)
    i = 2
    while i <= limit:
        if random_number % i == 0:
            return random_number, False
        i += 1
    return random_number, True


def brain_prime():
    name_user = welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i <= 3:
        random_number, prime = is_prime()
        right_answer = 'yes' if prime else 'no'
        print(f'Question: {random_number}')
        answer_user = answer()
        if answer_user == 'yes' and prime:
            print('Correct!')
            i = i + 1
        if answer_user == 'no' and not prime:
            print('Correct!')
            i = i + 1
        elif answer_user == 'no' and prime or answer_user == 'yes' \
        and not prime:
            return print(f"{answer_user} is wrong answer ;(. \
Correct answer was {right_answer}. \
\nLet's try again, {name_user}!")
    print(f'Congratulations, {name_user}!')
