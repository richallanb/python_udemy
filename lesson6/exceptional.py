"""
A module for demonstrating exceptions
"""
import sys
from math import log

def convert(s):
    '''Convert to an integer'''
    try:
        x = int(s)
    ## Can accept tuples for multiple exception types
    except (ValueError, TypeError):
        x = -1
    return x

def convert2(s):
    '''Convert to an integer'''
    x = -1
    try:
        x = int(s)
    ## Can accept tuples for multiple exception types
    except (ValueError, TypeError):
        pass
    return x

def convert3(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # log the exception
        print('Conversion error: {}'.format(str(e), file=sys.stderr))
        return -1

def string_log(s):
    # we eat the exception, but since we return -1, we create a new exception
    v = convert3(s)
    return log(v)

def convert4(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'.format(str(e), file=sys.stderr))
        # We can also bubble the exception up
        raise

def string_log2(s):
    # now we show the exception but still log a message
    v = convert4(s)
    return log(v)