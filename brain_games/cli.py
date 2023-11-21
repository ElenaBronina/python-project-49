import prompt


def welcome_user():
    name = prompt.string('brain-games\nWelcome to the Brain Games!\
                         \nMay I have your name? ')
    print(f'Hello, {name}!')


def main():
    welcome_user()


if __name__ == ('__main__'):
    main()
