import prompt

# NUMB ROUND
LVL = 3


# welcome message
def game_run(module):

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    # run welcome function from incoming module
    module.welcome()
    
    for lvl_char in range(LVL):
        # unpacking quest and answer funct. from incoming module
        quest_answer = module.question_answer()
        (question, answer) = quest_answer
        print(question)
        result = prompt.string("Your answer: ", empty=True)
        if result == answer:
            print("Currect!")
        else:
            print(
            f"'{result}' is wrong answer."
            f" Correct answer was '{answer}'\n"
            f"Let's try again, {name}!"
            )
            break
    else:
        print(f"Congratulations, {name}!")
