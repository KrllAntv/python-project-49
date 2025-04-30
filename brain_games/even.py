import random

import prompt


def even_numb(numb):
    result = ''
    if numb % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def even_game():
    score = 3
    index = 0
    name = prompt.string("May I have your name? ")
    print("Hello, " + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while index < score:
        random_numb = random.randint(1, 100)
        print('Question answer:', random_numb)
        result = prompt.string("Your answer: ", empty=True)
        if result == even_numb(random_numb):
            print("Currect!")
        else:
            print("\'" + result + "\'", 'is wrong answer. Correct answer was \''
            + even_numb(random_numb) + "\'.\nLet's try again,", name + "!")
            break
        index += 1
    if index == 3:
        print("Congratulations,", name + "!")



