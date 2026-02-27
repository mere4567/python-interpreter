# Builtins Module

# This file contains implementations of built-in functions and standard library functions for a Python interpreter.


def abs(x):
    """ Return the absolute value of a number. """
    return -x if x < 0 else x


def len(sequence):
    """ Return the number of items in a container. """
    count = 0
    for _ in sequence:
        count += 1
    return count


def max(*args):
    """ Return the largest of the input values. """
    return sorted(args)[-1]


def min(*args):
    """ Return the smallest of the input values. """
    return sorted(args)[0]

# Add more built-in functions and standard library implementations here.
