"""
File: anagram.py
Name: Lydia
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program commutes to finds all the anagram(s) for the word input by user.
    """
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        else:
            find_anagrams(s)  # start to find the anagrams
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():  # to read the dictionary text file
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.strip())  # put each data into a list without \n
    return dictionary


def find_anagrams(s):
    """
    :param s: a word given by user
    :return: N/A
    """
    print('Searching...')
    dict_ = read_dictionary()
    word_lst = []
    find_anagrams_helper(s, "", word_lst, dict_)  # a recursive helper function to find anagrams
    print(f'{len(word_lst)} anagrams: {word_lst}')


def find_anagrams_helper(s, current_s, word_lst, dictionary):
    """
    :param s: a word given by user
    :param current_s: the word that we combinate alphabets from s
    :param word_lst: a list which is composed of anagrams
    :param dictionary: a file of an English dictionary
    :return: N/A
    """
    if len(s) == 0:  # base case
        if current_s in dictionary:  # to check if the word(current_s) exists
            if current_s not in word_lst:
                word_lst.append(current_s)  # add it into anagrams list
                print('Found: ', current_s)
                print('Searching...')
    else:
        for i in range(len(s)):
            # choose
            current_s += s[i]
            unused_s = s[0:i] + s[i+1:]  # to choose from unused_s in next recursion
            # explore to check if need a early stop, if not, enter next recursion
            if has_prefix(current_s, dictionary):
                find_anagrams_helper(unused_s, current_s, word_lst, dictionary)
            # un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s, dictionary):
    """
    :param sub_s:
    :return:
    """
    for word in dictionary:
        if word.startswith(sub_s):  # to check if any word starts with sub_s
            return True
        else:
            pass
    return False


if __name__ == '__main__':
    main()
