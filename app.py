import random

text = open("poems/poem.txt", "r").read()


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
        random.choice(i)
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


def shuffle_words_on_line(line):
    """ Helper function which shuffles all words on a single line"""
    list_of_words = line.split(" ")
    random.shuffle(list_of_words)
    shuffled_line = " ".join(list_of_words)
    return shuffled_line


def shuffle_words_on_all_lines(lines):
    '''takes in all the lines. 
    shuffle the words on each line (by calling the helper function).
    Then returns the shuffled lines'''
    list_of_lines = lines.split("\n")
    for i in range(len(list_of_lines)):
        list_of_lines[i] = shuffle_words_on_all_lines(list_of_lines[i])
    shuffled_lines = "\n".join(list_of_lines)
    print(shuffled_lines)
    return shuffled_lines


def sort_by_abc_line(line):
    list_of_word = line.split(" ")
    alphabetical_order = " ".join(sorted(list_of_word))
    return alphabetical_order


def sort_by_abc_all_lines(lines):
    sorted_lines = []
    for line in lines:
        sorted_lines.append(sort_by_abc_line(line))
    print('\n'.join(sorted_lines))
    return '\n'.join(sorted_lines)


def user_choice():
    '''user choice funtion which allows the user to rquest which way the poem will be printed'''
    lines = text.lower().split("\n")
    poem_option = None
    options = ["backwards", "lines-random",
               "even-odd", "words-shuffle", "abc", "regular"]
    while poem_option not in options:
        poem_option = input(
            "Do you want the poem backwards, \nlines-random, \n sorted by even-odd,\n in alphabetical order,\n or If you just want to read a poem, type in regular:\n")

    if poem_option == "backwards":
        lines_printed_backwards(lines)
    elif poem_option == "lines-random":
        lines_printed_random(lines)
    elif poem_option == "even-odd":
        my_own_rearrange(lines)
    elif poem_option == "words-shuffle":
        shuffle_words_on_all_lines(lines)
    elif poem_option == "abc":
        sort_by_abc_all_lines(lines)
    elif poem_option == "regular":
        print(text)


user_choice()
