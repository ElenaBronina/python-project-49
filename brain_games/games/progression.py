import random
from brain_games.logic import answer
from brain_games.logic import welcome


def progression():
    length_progression = random.randint(5, 10)
    start_progression = random.randint(50, 100)
    step_progression = random.choice(range(2, 10))
    progression = [i for i in range(start_progression,
                                    length_progression * step_progression
                                    + start_progression,
                                    step_progression)]
    index_in_progression = progression.index(random.choice(progression))
    number_in_progression = progression[index_in_progression]
    return (progression, index_in_progression, number_in_progression)


def brain_progression():
    name_user = welcome()
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        game_conditions = progression()
        question_user = game_conditions[0]
        right_answer = game_conditions[2]
        question_user[game_conditions[1]] = '..'
        finally_question = ' '.join(str(x) for x in question_user)
        print(f'Question: {finally_question}')
        answer_user = answer()
        if answer_user != str(right_answer):
            return print(f"{answer_user} is wrong answer ;(. \
Correct answer was {right_answer}. \
\nLet's try again, {name_user}!")
        print('Correct!')
        i = i + 1
    print(f'Congratulations, {name_user}!')
