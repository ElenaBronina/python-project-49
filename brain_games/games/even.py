#!/usr/bin/env python3
import prompt
import random
from brain_games.games.logic import welcome


def question():
    question = random.choice(range(1, 100))
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    yes = question % 2 == 0 and answer == 'yes'
    no = question % 2 != 0 and answer == 'no'
    return ((yes or no), answer, question)


def even_number():
    name_user = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        start_game = question()
        if start_game[0] is False:
            if start_game[2] % 2 == 0:
                right_answer = 'yes'
            else:
                right_answer = 'no'
            return print(f"{start_game[1]} is wrong answer ;(.\
            Correct answer was {right_answer}.\nLet's try again, {name_user}!")
        print('Correct!')
        i = i + 1
    return print(f'Congratulations, {name_user}!')
