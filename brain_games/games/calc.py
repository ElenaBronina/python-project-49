import random
from brain_games.games.logic import answer
from brain_games.games.logic import welcome


def sum():
    a = random.choice(range(0, 100))
    b = random.choice(range(0, 100))
    return ((a + b), str(a) + "+" + str(b))
    

def diff():
    c = random.choice(range(50, 100))
    d = random.choice(range(0, 50))
    return ((c - d), str(c) + "-" + str(d))
    

def mult():
    e = random.choice(range(0, 10))
    f = random.choice(range(0, 10))
    return ((e * f), str(e) + "*" + str(f))
    

def random_choice():
    x = sum()
    y = diff()
    z = mult()
    list = [x, y, z]
    return random.choice(list)

    
def brain_calc():
    name_user = welcome()
    print(f'What is the result of the expression?')
    i = 1
    while i <= 3:
        random_question = random_choice() 
        question_user = random_question[1]
        right_answer = random_question[0]
        print(f'Question: {question_user}') 
        answer_user = answer()
        if answer_user != str(right_answer):
            return print(f"{answer_user} is wrong answer ;(. Correct answer was {right_answer}. Let's try again, {name_user}")
        print('Correct!')
        i = i + 1
    print(f'Congratulations, {name_user}!')
