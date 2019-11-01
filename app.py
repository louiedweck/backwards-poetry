import random

poem = '''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference
'''

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
    ''' Function of your choice that rearranges the poem in a unique way'''
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
            "Do you want the poem backwards, \n lines-random, \n or sorted by even-odd.\n If you just want to read a poem, type in anyting else:\n")

    if poem_option == "backwards":
        lines_printed_backwards(lines)
    elif poem_option == "lines-random":
        lines_printed_random(lines)
    elif poem_option == "even-odd":
        my_own_rearrange(lines)
    elif poem_option == "regular":
        print(poem)


user_choice()
