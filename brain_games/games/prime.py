import random


def welcome():
    print(
        "Answer \"yes\" if given number is prime.",
        "Otherwise answer \"no\".",
        )


# prime number determination function
def find_prime_numb(numb):
    divide = 0
    for _ in range(1, numb + 1):
        if numb % _ == 0:
            if numb == 1:
                return 'no'
            divide += 1
    if divide > 2:
        return 'no'
    else:
        return 'yes'
            

def question_answer():
    numb = random.randint(1, 41) 
    answer = find_prime_numb(numb)
    question = f'Question: {numb}'
    result = (question, answer)
    return result