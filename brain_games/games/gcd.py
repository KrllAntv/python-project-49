import math
import random

# Message game
def welcome():
    print("Find the greatest common divisor of given numbers.")

def question_answer():
    numb1 = random.randint(1, 100)
    numb2 = random.randint(1, 100)
    answer = math.gcd(numb1, numb2)
    question = f'Question: {numb1} {numb2}'
    resutl = (question, str(answer))
    return resutl
