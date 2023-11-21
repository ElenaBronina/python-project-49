import prompt


def welcome():
    name_user = prompt.string('Welcome to the Brain Games!\
                              \nMay I have your name?')
    print(f'Hello, {name_user}!')
    return name_user


def answer():
    answer = prompt.string('Your answer: ')
    return answer
