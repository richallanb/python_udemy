#!/usr/bin/env python3
# ^-- Doesn't create a problem in windows for binding to python executor
"""Retrieve and print words from a URL.

Usage:
    python words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from 
        the document.
    """
    # Docstring documentation
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    # Scope is not bound inside operators like for, if, while, etc.
    print(word)
    return story_words

def print_items(items):
    """Print items on per line.

    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)

def main(url = 'http://sixty-north.com/c/t.txt'):
    """Print each word from a text document

    Args:
        url: The URL of a UTF-8 text document
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1]) #0th argument is the python module name
    else:
        main()
