import unittest
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
# TODO: get a list of strings that contains lines of poem
lines = poem.split("\n")
# print(lines)


def lines_printed_backwards(lines):
    '''This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed. --> function stub'''
    backwards = list(reversed(lines))
    for index, line in enumerate(backwards):
        print(index, line[::-1])

    return backwards


class PoetryTest(unittest.TestCase):

    def test_lines_printed_backwards(self):
        assert list(reversed(lines)) == lines_printed_backwards(lines)


def lines_printed_random(lines):
    '''Function which will randomly select lines from a list of strings and print them out in random order.
    '''
    pass


def my_own_rearrange():
    ''' Function of your choice that rearranges the poem in a unique way'''
    pass


if __name__ == '__main__':
    unittest.main()
