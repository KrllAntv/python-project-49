import random


def welcome():
    print(
        "Answer \"yes\" if given number is prime.",
        "Otherwise answer \"no\".",
        )


# prime number determination function
def is_prime(numb):
    divide = 0
    for _ in range(1, numb + 1):
        if numb % _ == 0:
            if numb == 1:
                return False
            divide += 1
    if divide > 2:
        return False
    else:
        return True
            

def question_answer():
    numb = random.randint(1, 41) 
    answer = 'yes' if is_prime(numb) is True else 'no'
    question = f'Question: {numb}'
    result = (question, answer)
    return result