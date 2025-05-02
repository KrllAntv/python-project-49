import random


def welcome():
    print(
        f"Answer \"yes\" if given number is prime.",
        f"Otherwise anser \"no\"",
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
        return f'no'
    else:
        return f'yes'
        

def question_answer():
    numb = random.randint(1, 41) 
    answer = find_prime_numb(numb)
    question = f'Question: {numb}'
    result = (question, answer)
    return result