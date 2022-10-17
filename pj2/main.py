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

def simulator():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)

    return dice_1, dice_2


def craps():
    dice_2, dice_1 = simulator()
    _sum = sum([dice_2, dice_1])

    print(f'{dice_1} + {dice_2} = {_sum}')
    if _sum in [7, 11]:
        print('wins player')

    elif _sum in [2, 3, 12]:
        print('wins casino')

    else:
        goal = _sum
        print('goal', goal)
        while True:
            dice_2, dice_1 = simulator()
            _sum = sum([dice_2, dice_1])
            print(f'{dice_1} + {dice_2} = {_sum}')

            if _sum == goal:
                print('wins player')
                break
            elif _sum == 7:
                print('wins casino')
                break


if __name__ == '__main__':
    craps()
