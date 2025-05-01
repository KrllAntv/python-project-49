import random
from operator import add, mul, sub


# Messag game
def welcome():
    print("What is the result of the expression?")


def question_answer():
    symbol, operation = random.choice((
    ('+', add),
    ('*', mul),
    ('-', sub),
    ))
    numb1 = random.randint(1, 10)
    numb2 = random.randint(1, 10)
    answer = operation(numb1, numb2)
    question = f'Question: {numb1} {symbol} {numb2}'
    result = (question, str(answer))
    return result