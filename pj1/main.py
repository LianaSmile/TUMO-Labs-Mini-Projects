from random import choice

"""
Station Project 1 : Mad Libs

The task

Write a program on Python that does the following:
1. Allows the user to pick one of the templates
2. Asks the user to input words. “Type number”, for example
3. Generate a story afterwards and shows it to the user
"""

TEMPLATES = [
    {
        'number': '1',
        'template': 'It was about {number} {measure_of_time} ago when I arrived at the hospital in a '
                    '{mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of '
                    '{adjective2} {noun} here. There are nurses here who have {color} {part_of_the_body}. '
                    'If someone wants to come into my room I told them that they have to {verb} first. '
                    'I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they '
                    'were wearing a {noun3} on their {part_of_the_body2}. I heard that all doctors {verb2} '
                    '{noun4} every day for breakfast. The most {adjective3} thing about being in the '
                    'hospital is the {silly_word} {noun5}!',
        'questions': {
            'number': 'Number',
            'measure_of_time': 'Measure of time',
            'mode_of_transportation': 'Mode of Transportation',
            'adjective': 'Adjective',
            'adjective2': 'Adjective',
            'noun': 'Noun',
            'color': 'Color',
            'part_of_the_body': 'Part of the Body',
            'verb': 'Verb',
            'number2': 'Number',
            'noun2': 'Noun',
            'noun3': 'Noun',
            'part_of_the_body2': 'Part of the Body',
            'verb2': 'Verb',
            'noun4': 'Noun',
            'adjective3': 'Adjective',
            'silly_word': 'Silly Word',
            'noun5': 'Noun',
        }
    },
    {
        'number': '2',
        'template': 'This weekend I am going camping with {proper_noun}. I packed my '
                    'lantern, sleeping bag, and {noun}. I am so {adjective} to {verb} in a tent. '
                    'I am {adjective2} we might see a(n) {animal}, I hear they’re kind of '
                    'dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have '
                    'heard that the {color} lake is great for {verb3}. Then we will '
                    '{adverb} hike through the forest for {number} {measure_of_time}. '
                    'If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! '
                    'At night we will tell {number2} {silly_word} stories and roast {noun2} around the '
                    'campfire!!',
        'questions': {
            'proper_noun': 'Person’s Name',
            'noun': 'Noun',
            'adjective': 'Adjective (Feeling)',
            'verb': 'Verb',
            'adjective2': 'Adjective (Feeling)',
            'animal': 'Animal',
            'verb2': 'Verb',
            'color': 'Color',
            'verb3': 'Verb (ending in ing)',
            'adverb': 'Adverb (ending in ly)',
            'number': 'Number',
            'measure_of_time': 'Measure of time',
            'color2': 'Color',
            'animal2': 'Animal',
            'number2': 'Number',
            'silly_word': 'Silly Word',
            'noun2': 'Noun',
        }
    },
    {
        'number': '3',
        'template': 'Dear {proper_noun}, I am writing to you from a {adjective} castle '
                    'in an enchanted forest. I found myself here one day after going for a ride on a '
                    '{color} {animal} in {place}. There are {adjective2} {magical_creature} '
                    'and {adjective3} {magical_creature2} here! In the {room_in_a_house} there '
                    'is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun3} '
                    'and dream of {adjective4} {noun4}. It feels as though I have lived here for '
                    '{number} {measure_of_time}. I hope one day you can visit, although the only way to get'
                    ' here now is {verb} on a {adjective5} {noun5}!!',
        'questions': {
            'proper_noun': 'Person’s Name',
            'adjective': 'Adjective',
            'color': 'Color',
            'animal': 'Animal',
            'place': 'Place',
            'adjective2': 'Adjective',
            'magical_creature': 'Magical Creature (Plural)',
            'adjective3': 'Adjective',
            'magical_creature2': 'Magical Creature (Plural)',
            'room_in_a_house': 'Room in a House',
            'noun': 'Noun',
            'noun2': 'Noun',
            'noun3': 'Noun (Plural)',
            'adjective4': 'Adjective',
            'noun4': 'Noun (Plural)',
            'number': 'Number',
            'measure_of_time': 'Measure of time',
            'verb': 'Verb (ending in ing)',
            'adjective5': 'Adjective',
            'noun5': 'Noun',
        }
    }
]


def process_template(template):
    """
    This function receives the chosen template's number, and collects answers for corresponding questions from the user.
    Then adds the answers to the template and returns the final text.
    """
    for key, value in template.get('questions').items():
        template['questions'][key] = input(f'Type {value}: ')

    text = template.get('template')
    answers = template.get('questions')

    return text.format(**answers)


def validation(answer):
    """
    This functions receives user's input and validates its.
    """
    if answer.lower() in ['r', 'random']:
        validation_answer = choice(TEMPLATES)

    elif answer.lower() in ['s', 'stop']:
        validation_answer = 'stop'

    elif answer.isdigit() and int(answer) in range(1, len(TEMPLATES) + 1):
        validation_answer = TEMPLATES[int(answer) - 1]

    else:
        validation_answer = 'continue'

    return validation_answer


def mad_libs():
    """
    This is the main function which starts the game, calls corresponding functions and prints final result.
    """

    print(' Welcome to Station Project 1 : Mad Libs! '.center(110, '~'), '\n')

    while True:
        answer = input(f"Type template number from 1 to {len(TEMPLATES)} or just type r/random to choose a template!"
                       f"(to exit the program type s/stop): ")

        answer = validation(answer)

        if answer == 'stop':
            print('\nThank you and bye-bye!!')
            break
        elif answer == 'continue':
            print('\nInvalid input try again!!!')
            continue

        else:
            print(f'\nYou have chosen template number {answer.get("number")}, please, type the needed words.')
            result = process_template(answer)
            print('\n', result)


if __name__ == '__main__':
    mad_libs()
