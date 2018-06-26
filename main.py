""" 
	The purpose of this python script:
	1 - To count the words in a file
	2 - Sort the counts 
	3 - Write them to a txt file in decreasing order

	Ex:
	file.txt>> 
		Hello world. My name is computer. I am very curious about you. 
		kerem kerem kerem
		arif, .arif,., .,,arif,.. ,.arif:: :arif

	counts.txt>>
		arif: 5
		kerem: 3
		hello: 1
		my: 1
		you: 1
		world: 1
		curious: 1
		computer: 1
		very: 1
		am: 1
		is: 1
		i: 1
		name: 1
		about: 1
"""

import argparse
import operator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z']


def add_to_dict(word, dict):
	try:
		#if the word is present in the dict then val ++
		dict[word] = dict[word] + 1
	except:
		# if the word is not present in the dict -> creates a key for that word and sets the value to 1
		dict[word] = 1
	
def is_included(char, arr):
	for element in arr:
		if char == element:
			return True
	return False

def run():

	parser = argparse.ArgumentParser()
	# the --file argument is for the file name, if you don't want to change the file name or type you can use this arg
	parser.add_argument('--file', help='path for file to read', default = 'file.txt')
	# the --dest argument is for the destination file name
	parser.add_argument('--dest', help='path for destination file', default = 'counts.txt')

	args = parser.parse_args()

	word_counts = {}

	with open(args.file) as file:

		word = ''

		while True:
			# reads a single character
			char = file.read(1)
			
			if char == ' ' or char == '\n':
				# if the word is empty don't add it to the list
				if not word == '':	
					add_to_dict(word, word_counts)
					word = ''

			elif(is_included(char, letters)):
				# if the char is lowercase then appends it to the word
				word += char

			elif(is_included(char, upper_case_letters)):
				# if the char is uppercase letter then turns it into a lowercase then appends it
				lowercase = letters[upper_case_letters.index(char)]
				word += lowercase

			if not char:
				# adds the last word to the dictionary
				if not word == '':	
					add_to_dict(word, word_counts)
				break

	# puts the dictionary into an array then sorts it (from low to high)
	sorted_dict = sorted(word_counts.items(), key = operator.itemgetter(1))

	with open(args.dest, 'w') as counts:

		for i in range(len(sorted_dict)):
			# we want it written from high to low that's why the index is len(sorted_dict) - 1 - i
			key, value = sorted_dict[len(sorted_dict) - 1 - i]
			counts.write(key + ': ' + str(value)+ '\n')

		# for unsorted print use this 	
		# for key, value in word_counts.items():
		# 	counts.write(key + ': ' + str(value)+ '\n')

if __name__ == '__main__':
	run()