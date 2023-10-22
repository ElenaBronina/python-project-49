import prompt

def welcome_user():
    name = prompt.string(f'brain-games\nWelcome to the Brain Games!\nMay I have your name?')
    print (f'Hello, {name}!')