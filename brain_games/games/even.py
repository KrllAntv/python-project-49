import random


def welcome():
    print(
        "Answer \"yes\" if given number is prime.",
        "Otherwise anser \"no\"",
        )


def even_numb(numb: int):
    if numb % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question_answer():
    random_numb = random.randint(1, 100)
    answer = even_numb(random_numb)
    question = f'Question: {random_numb}'
    result = (question, answer)
    return result