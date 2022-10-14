from random import randint

"""
Station Project 2 : Craps

The task

Here are the rules of the game:

The player should roll two dice. If the sum of both of them is 7 or 11 the player wins.
If the sum is 2, 3 or 12 (craps) the casino wins. If during the first roll the sum is
4, 5, 6, 8, 9 or 10, that number becomes the “goal” number. To win, the player should
roll the dice till they roll the goal number again. If the player rolls a 7 before rolling
the goal number, they lose.

Your task is to recreate this game using Python. Your program should roll two dice and
output the sum of two random numbers. By following the rules of the game, your program
should decide whether the player wins or loses.
"""

ROLLS_COUNT = 0
GOAL = 'Not Set'


def simulator():
    """
    This function generates 2 random number for each dice.
    """
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)

    return dice_1, dice_2


def check_the_sum(dices):
    """
    This function checks the roll number and sets goals number if needed, then checks who wins, returns answer.
    """
    global GOAL
    sum_of_dices = sum(dices)

    if ROLLS_COUNT == 1 and sum_of_dices in [4, 5, 6, 8, 9, 10]:
        GOAL = sum_of_dices

    if GOAL is None:
        if sum_of_dices in [7, 11]:
            game_answer = 'Congratulations, you win!'
        elif sum_of_dices in [2, 3, 12]:
            game_answer = 'Alas, Casino wins!'
        else:
            game_answer = 'No one wins!'
    else:
        if sum_of_dices is GOAL:
            game_answer = 'Congratulations, you win!'
        elif sum_of_dices == 7:
            game_answer = 'Alas, Casino wins!'
        else:
            game_answer = f'Keep, going, the goal number is {GOAL}!'

    return game_answer, sum_of_dices, GOAL


def craps():
    """
    This function calls the corresponding functions and prints the final result.
    """
    global ROLLS_COUNT
    while True:
        ROLLS_COUNT += 1
        dices = simulator()
        answer, sum_of_dices, goal = check_the_sum(dices)
        print('~' * 50)
        print(f'Game answer: {answer}\nSum of dices: {sum_of_dices}\nGOAL number: {goal}\n')
        one_more = input('Want one more round?(y/n): ')
        if one_more.lower() == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    craps()
