import random

from functions import lines_printed_backwards
from functions import lines_printed_random
from functions import my_own_rearrange
from functions import shuffle_words_on_all_lines
from functions import sort_lines_by_abc
from functions import sort_by_length_of_line
from functions import valid_user_input
from functions import first_letter_abc_order


text = open("poems/poem.txt", "r").read()


def user_choice():
    '''user choice funtion which allows the user to rquest which way the poem will be printed'''
    lines = text.lower().split("\n")
    question = '''
            Do you want the poem backwards,
            random,
            sorted by even-odd,
            alphabetical order (abc),
            line length (ll),
            words shuffled (ws),
            first letter on the line (fl)
            or if you just want to read a poem, type in r: '''
    answers = ["backwards", "random",
               "even-odd", "ws", "abc", "ll", "fl", "r"]

    poem_option = valid_user_input(question, answers)

    if poem_option == "backwards":
        lines_printed_backwards(lines)
    elif poem_option == "lines-random":
        lines_printed_random(lines)
    elif poem_option == "even-odd":
        my_own_rearrange(lines)
    elif poem_option == "words-shuffle":
        shuffle_words_on_all_lines(lines)
    elif poem_option == "abc":
        sort_lines_by_abc(lines)
    elif poem_option == "ll":
        sort_by_length_of_line(lines)
    elif poem_option == "fl":
        first_letter_abc_order(lines)
    elif poem_option == "r":
        print(text)


if __name__ == '__main__':
    user_choice()
# lines = text.split("\n")
# print(sort_by_length_of_line(lines))
# sort_by_length_of_line(lines)
