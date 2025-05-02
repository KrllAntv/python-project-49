import random


def welcome():
    print("What number is missing in the progression?")


def question_answer():
    numb = random.randint(5, 10)
    random_step = random.randint(2, 5)
    index = 0
    progress = []
    while len(progress) < numb:
        progress.append(numb + index)
        index += random_step   
    answer = random.choice(progress)
    ind = progress.index(answer)
    progress[ind] = '..'
    string = ' '.join(map(str, progress))
    question = f'Question: {string}'
    result = (question, str(answer))
    return result