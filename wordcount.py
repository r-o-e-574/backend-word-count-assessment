#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Ruben Espino I got help from Doug Enas and used this site https://www.geeksforgeeks.org/python-get-top-n-elements-from-records/ to figure out the last problem and some help from Chris Warren"

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    wordCount = {}
    with open(filename, 'r') as textfile:
        for line in textfile.readlines():
            for word in line.split():
                if word in wordCount:
                    wordCount[word.lower()] += 1
                else:
                    wordCount[word.lower()] = 1
    return wordCount

def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    word_dict = create_word_dict(filename)
    wordList = []
    for key in word_dict:
        wordList.append(key)
        print(key, ":", word_dict[key])
    return sorted(wordList)


def print_top(filename):
    """Prints the top count listing for the given file."""
    word_dict = create_word_dict(filename)
    top_list = sorted(word_dict, key = lambda word: word_dict[word], reverse = True)[:20]
    for key in top_list:
        print(key, ":", str(word_dict[key]))
    return top_list
    
    


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)
 
    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
