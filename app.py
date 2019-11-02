import random

poem = open("poems/poem.txt", "r").read()
lines = poem.split("\n")


def lines_printed_backwards(lines):
    '''This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed. --> function stub'''
    backwards = list(reversed(lines))
    for index, line in enumerate(backwards):
        print(index, line[::-1])

    return backwards


random_lines_poem = []


def lines_printed_random(lines):
    '''Function which will randomly select lines from a list of strings and print them out in random order.
    '''
    for i in range(len(lines)):
        random.choice(lines)
        random_lines_poem.append(random.choice(lines))
    print(random_lines_poem)


def my_own_rearrange(lst):
    ''' Function that sorts poem by even and odd lines. Proceeds to add the even lines to one list and the odds to another. Finally prints even list and then odd list.'''
    evens = []
    odds = []
    for i in range(len(lst)):
        if i % 2 == 0:
            evens.append(lst[i])
        else:
            odds.append(lst[i])
    print(evens + odds)
    return evens + odds


def user_choice():
    poem_option = None
    options = ["backwards", "lines-random", "even-odd", "regular"]
    while poem_option not in options:
        poem_option = input(
            "Do you want the poem backwards, \nlines-random, \nor sorted by even-odd.\nIf you just want to read a poem, type in regular:\n")

    if poem_option == "backwards":
        lines_printed_backwards(lines)
    elif poem_option == "lines-random":
        lines_printed_random(lines)
    elif poem_option == "even-odd":
        my_own_rearrange(lines)
    elif poem_option == "regular":
        print(poem)


user_choice()
