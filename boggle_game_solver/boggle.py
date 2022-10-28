"""
File: boggle.py
Name: Lydia
----------------------------------------
Boggle is a word game which random letters are put in a 4x4 tray. Players need to find all the words that they could
connect through these letters. Now we are gonna design this game via Python.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program computes to play the Boggle game using the given letters from user input.
	Rules included:
	1.Words must be at least 4 letters in length.
	2.Each letter after the first must be a horizontal, vertical or diagonal neighbor of the one before it.
	3.No individual letter may be used more than once in a word.
	4.The letters from user input need to be 4 letters with 1 space between each letter at a time.
	"""
	start = time.time()
	ch_total = []  # gonna put 16 letters from user input in this list.
	count = 0  # to check if user successfully input 4 rows of letters.
	for i in range(4):
		row = input(str(i+1) + ' row of letters: ')
		if len(row) > 7 or row[1] is not ' ' or row[3] is not ' ' or row[5] is not ' ' or row[0].isalpha() is not True or row[2].isalpha() is not True or row[4].isalpha() is not True or row[6].isalpha() is not True:
			print('Illegal input')
			break
		count += 1
		row = row.lower()  # type_string
		ch = row.split()  # type_list
		for j in range(4):
			ch_total.append(ch[j])

	if count == 4:
		# make each letter as a coordinate
		ch_dict = {}
		for i in range(4):
			for j in range(4):
				ch_dict[(i, j)] = ch_total[i * 4 + j]  # key-coordinate(i, j) indicates value-letter
				# ch_dict[(i, j)] = ch_total[i + 4*j]

		dictionary = read_dictionary()
		word_total = []  # a list of all words we find from the given characters
		for i in range(4):  # the centered 'letter'
			for j in range(4):
				cor_lst = []  # a list of coordinates of used letter
				ch = ch_dict[(i, j)]
				cor_lst.append((i, j))
				find_word(ch, i, j, ch_dict, dictionary, word_total, cor_lst)

		print('There are ' + str(len(word_total)) + ' words in total.')
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())  # put each data into a list without \n
	return dictionary


def find_word(current_word, x, y, ch_dict, dict, word_total, cor_lst):
	"""
	current_word: string
	"""
	for k in range(-1, 2, 1):  # to find its neighbors
		for l in range(-1, 2, 1):
			if 0 <= x + k < 4:  # make sure the coordinate is within 4x4
				if 0 <= y + l < 4:  # make sure the coordinate is within 4x4
					if (x + k, y + l) not in cor_lst:  # to check if the coordinate was used in this word
						cor_lst.append((x + k, y + l))
						if len(current_word) >= 4:
							if current_word in dict:
								if current_word in word_total:
									pass
								else:
									print(f'Found "{current_word}"')
									word_total.append(current_word)
						# choose
						ch = ch_dict[(x + k, y + l)]
						current_word += ch
						# explore
						if has_prefix(current_word, dict):
							find_word(current_word, x + k, y + l, ch_dict, dict, word_total, cor_lst)
						# un-choose
						current_word = current_word[:-1]  # remove the last letter in the word
						cor_lst.pop()  # remove the coordinate of the last letter from the coordinate list



def has_prefix(sub_s, dict):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
