import random

import prompt


def even_numb(numb: int):
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
    print(f'Hello {name}')
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while index < score:
        random_numb = random.randint(1, 100)
        print(f"Question answer: {random_numb}")
        result = prompt.string("Your answer: ", empty=True)
        if result == even_numb(random_numb):
            print("Currect!")
        else:
            print(
            f"'{result}' is wrong answer."
            f" Correct answer was '{even_numb(random_numb)}'\n"
            f"Let's try again, {name}!"
            )
            break
        index += 1
    if index == 3:
        print(f"Congratulations {name}!")
